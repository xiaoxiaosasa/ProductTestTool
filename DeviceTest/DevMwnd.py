# -*- coding: UTF-8 -*-
# author:yuliang

import logging
from logging import handlers,Formatter
import time
from _thread import start_new_thread
from threading import RLock

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot

from DeviceTest.Casher import Casher
from DeviceTest.GPIO import GPIO
from DeviceTest.scanner import ScannerInterface
from DeviceTest.Printer import Printer
from DeviceTest.serialPort import Connect
from DeviceTest.voice import Speaker

import json
from DeviceTest.Music  import *

CFG = json.load(open('config.json', 'r+', encoding='utf-8'))
isEntry = CFG["isEntry"]
logger = logging.getLogger()

class DevMwnd(QtGui.QDialog):
    PRINTSTATUS = QtCore.SIGNAL("PRINTSTATUS(bool)")
    SCANNERSTATUS = QtCore.SIGNAL("SCANNERSTATUS(QString)")
    CASHTEST = QtCore.SIGNAL("CASHTEST(int,QString)")
    LEVELCHANGE = QtCore.SIGNAL("LEVELCHANGE(int,QString)")
    OUT = QtCore.SIGNAL("OUT(int)")
    VOICESTATUS =QtCore.SIGNAL("VOICESTATUS")
    PORTCONNECT = QtCore.SIGNAL('PORTCONNECT(QString)')

    LOGPRINT = QtCore.SIGNAL("LOGPRINT(QString)")

    def __init__(self):
        QtGui.QDialog.__init__(self, parent=None)
        uic.loadUi("DeviceTest/DevMwnd.ui", self)

        self.Casherstatus = [-1, -1,-1]
        self.logUi = LogUi(self.logListView)

        self.infoLock = RLock()

        QtCore.QObject.connect(self, self.PRINTSTATUS, self.__PrinterConfirm)
        QtCore.QObject.connect(self, self.SCANNERSTATUS, self.__ScannerConfirm)
        QtCore.QObject.connect(self, self.CASHTEST, self.__CasherConfirm)
        QtCore.QObject.connect(self, self.LEVELCHANGE, self.__GPIOKeyConfirm)
        QtCore.QObject.connect(self, self.OUT, self.__OutConfirm)
        QtCore.QObject.connect(self,self.VOICESTATUS,self.__voiceConfirm)
        QtCore.QObject.connect(self,self.PORTCONNECT,self.__connectConfirm)

        QtCore.QObject.connect(self, self.LOGPRINT, self.logUi.log)


        self.speaker = Speaker(self)
        self.speaker.start()
        self.scannerMC = None
        self.casherMC = None
        self.GPOMC1 = None
        self.printerMC = None
        self.music = None


    def closeEvent(self, QCloseEvent):
        '''强制退出,若非如此，关闭主窗口时残留的线程会继续运行'''
        import os
        os._exit(0)

    @pyqtSlot()
    def on_serialPort12_clicked(self):
        self.serialPort.setDisabled(True)
        con = Connect("com1","com2",self)
        con.start()

    @pyqtSlot()
    def on_serialPort34_clicked(self):
        self.serialPort.setDisabled(True)
        con = Connect("com3", "com4", self)
        con.start()  # 这里会不会卡有待查证

    def __connectConfirm(self,rst):
        if rst == "true":
            self.logUI('%s-%s串口测试成功'%(self.port1.port,self.port2.port))
            self.serialPort.setStyleSheet("background-color: green")
        else:
            self.serialPort.setStyleSheet("background-color: red")
            self.logUI('%s-%s串口测试成功'%(self.port1.port,self.port2.port))
        self.serialPort.setDisabled(False)


    @pyqtSlot()
    def on_voiceBtn_clicked(self):
        self.voiceBtn.setDisabled(True)
        self.voiceBtn.setStyleSheet("background-color: rgb(86,86,86)")

        # start_new_thread(self.speaker.test,('wellcome go to china,欢迎来中国',))
        self.music = Music()
        start_new_thread(self.music.play,(CFG['mp3'],))
        rst = QtGui.QMessageBox.question(self, "提问", '请确认是否听到声音', '是', '否')

        self.infoLock.acquire()
        self.music.isRunning = False
        self.infoLock.release()

        if rst == 0:
            self.voiceBtn.setText('测试成功')
            self.voiceBtn.setStyleSheet("background-color: green")
            self.logUi.log("语音测试成功")
        else:
            self.voiceBtn.setText('测试失败')
            self.voiceBtn.setStyleSheet("background-color: red")
            self.logUi.log("语音测试失败")
        self.voiceBtn.setDisabled(False)

    def __voiceConfirm(self):
        rst = QtGui.QMessageBox.question(self,"提问",'请确认是否听到声音','是','否')
        if rst ==0:
            self.voiceBtn.setText('测试成功')
            self.voiceBtn.setStyleSheet("background-color: green")
            self.logUi.log("语音测试成功")
        else:
            self.voiceBtn.setText('测试失败')
            self.voiceBtn.setStyleSheet("background-color: red")
            self.logUi.log("语音测试失败")
        self.voiceBtn.setDisabled(False)


    @pyqtSlot()
    def on_PrinterTest_clicked(self):
        self.printer = Printer(self)
        if self.printer.port:
            start_new_thread(self.printer.printRaw,
                             ('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '线上支付', '2019-3-24-10:30:45',
                              '2019-3-24-1:30:51', 'http://www.baidu.com'))
            # printer.printRaw('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '现金支付', '2019-3-24-10:30:45',
            #                                       '2019-3-24-1:30:51', '找零2.4元')

            self.PrinterTest.setDisabled(True)

    def __PrinterConfirm(self,isError):
        '''打印机状态确认'''
        # Speaker.speak("请确认打印是否正确")
        if isError:
            rst = 1
        else:
            rst = QtGui.QMessageBox.warning(self, "确认", '请确认打印是否正确', '正确', '错误')
        self.PrinterTest.setDisabled(False)
        self.setPrinterAndScanStatus(rst, self.PrinterStatus, '打印机')

    @pyqtSlot()
    def on_RMB5Test_clicked(self):
        if isEntry == 'True':
            self.logUi.log("入口无吃钞机，无需测试！")
            return
        self.RMB5Test.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.casher = Casher(CFG['casherCom'], self)
        if self.casher.isopen== 1:
            self.CasherStatus.setStyleSheet("background-color: rgb(255, 255, 0)")
            self.CasherStatus.setText('测试中...')
            self.RMB5Test.setDisabled(True)
            self.RMB10Test.setDisabled(True)
            self.ErrTestBtn.setDisabled(True)
            start_new_thread(self.casher.TestMoney, (5,))

         #   start_new_thread(self.setOutTime, ("casher",20,))
            # Speaker.speak('请放入5元钞票')
            self.speaker.speak("等待放入5元钞票")
            self.__manulAskDlg("提示", "等待放入5元钞票")

    @pyqtSlot()
    def on_RMB10Test_clicked(self):
        if isEntry == 'True':
            self.logUi.log("入口无吃钞机，无需测试！")
            return
        self.RMB10Test.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.casher = Casher(CFG['casherCom'], self)

        if self.casher.isopen == 1:
            self.CasherStatus.setStyleSheet("background-color: rgb(255, 255, 0)")
            self.CasherStatus.setText('测试中...')
            self.RMB5Test.setDisabled(True)
            self.RMB10Test.setDisabled(True)
            self.ErrTestBtn.setDisabled(True)
            start_new_thread(self.casher.TestMoney, (10,))

        # start_new_thread(self.setOutTime, ("casher",20,))
        # Speaker.speak('请放入10元钞票')
            self.speaker.speak("等待放入十元钞票")
            self.__manulAskDlg("提示", "等待放入10元钞票")

    @pyqtSlot()
    def on_ErrTestBtn_clicked(self):
        if isEntry== 'True':
            self.logUi.log("入口无吃钞机，无需测试！")
            return
        self.ErrTestBtn.setStyleSheet("background-color: rgb(86,86,86)")
        self.casher = Casher(CFG['casherCom'],self)

        if self.casher.isopen == 1:
            self.CasherStatus.setStyleSheet("background-color: rgb(255, 255, 0)")
            self.CasherStatus.setText('测试中...')
            self.RMB5Test.setDisabled(True)
            self.RMB10Test.setDisabled(True)
            self.ErrTestBtn.setDisabled(True)
            start_new_thread(self.casher.TestMoney,(100,))

        # start_new_thread(self.setOutTime,("casher",30,))
            self.speaker.speak("等待放入5元钞票")
            self.__manulAskDlg("提示", "等待放入5元钞票")


    def __CasherConfirm(self, cash, status):
        if cash==100:
            if status =="Err":
                self.setRMBStatus("true", self.__dict__["ErrTestBtn"], '错误测试')
            else:
                self.setRMBStatus("false", self.__dict__["ErrTestBtn"], '错误测试')
        else:
            RMB = 'RMB' + str(cash) + 'Test'
            self.setRMBStatus(status, self.__dict__[RMB], '吃钞机%d元测试' % (cash))
        # if cash==5:
        #     self.RMB10Test.setDisabled(False)
        # elif cash ==10:
        #     self.RMB5Test.setDisabled(False)
        self.RMB5Test.setDisabled(False)
        self.RMB10Test.setDisabled(False)
        self.ErrTestBtn.setDisabled(False)
        self.confirmDlg.done(0)

    def setRMBStatus(self, status, obj, param=None):
        '''设置钞票状态'''
        if status == "true":

            if obj is self.RMB5Test:
                self.Casherstatus[0] = True
            elif obj is self.RMB10Test:
                self.Casherstatus[1] = True
            elif obj is self.ErrTestBtn:
                self.Casherstatus[2]= True
            if param:
                self.logUi.log('%s正常' % param)
                # Speaker.speak('%s测试成功' % param)
            obj.setStyleSheet("background-color:green")
        else:
            if obj is self.RMB5Test:
                self.Casherstatus[0] = False
            elif obj is self.RMB10Test:
                self.Casherstatus[1] = False
            elif obj is self.ErrTestBtn:
                self.Casherstatus[2]=False
            if param:
                self.logUi.log('%s不通过' % param)
                # Speaker.speak('%s测试失败' % param)

            obj.setStyleSheet("background-color:red")

        if self.Casherstatus == [True, True,True]:
            self.CasherStatus.setText('测试成功')
            self.CasherStatus.setStyleSheet("background-color:green")
            self.Casherstatus = [-1, -1, -1]  #测试成功之后重新置回原状态
        elif -1 in self.Casherstatus:
            self.CasherStatus.setText('测试中...')
            self.CasherStatus.setStyleSheet("background-color:rgb(255,255,0)")
        else:
            self.CasherStatus.setText('NG')
            self.CasherStatus.setStyleSheet("background-color:red")



    @pyqtSlot()
    def on_ScanTest_clicked(self):
        if isEntry=='True':
            self.logUi.log("入口无扫码枪，无需测试！")
            return
        self.SanInfo.setText('')
        self.Scanstatus.setText('未测试')
        self.Scanstatus.setStyleSheet("background-color: rgb(86, 86, 86)")
        time.sleep(0.5)
        self.scanner = ScannerInterface(9600, self)
        if self.scanner.port:
            start_new_thread(self.scanner.test, ())
            self.ScanTest.setDisabled(True)
            self.speaker.speak("请扫描打印凭条的二维码")
            self.__manulAskDlg('提示', "请扫描打印凭条的二维码")




    def __ScannerConfirm(self, param):
        '''扫码枪状态确认'''
        self.SanInfo.setText(str(param))
        if str(param) == CFG['scanInfo']:
            rst = 0
        else:
            rst = 1
        self.ScanTest.setDisabled(False)
        self.setPrinterAndScanStatus(rst, self.Scanstatus, '扫码枪')
        self.confirmDlg.done(0)


    def setPrinterAndScanStatus(self, rst, obj, param):
        '''设置扫码枪和打印机状态'''
        if rst == 0:
            self.logUi.log('%s测试正常' % param)
            obj.setText('测试成功')
            obj.setStyleSheet("background-color:green")

        else:
            self.logUi.log('%s测试不通过' % param)
            obj.setText('NG')
            obj.setStyleSheet("background-color:red")


    @pyqtSlot()
    def on_key1_clicked(self):
        self.key1.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.call = GPIO(self)
        if self.call.isRunning:
            self.key1.setDisabled(True)
            start_new_thread(self.call.Inlevel_Down, (CFG["key1"][0],))
            # start_new_thread(self.setOutTime,("Call",10))
          #  QtGui.QMessageBox.about(self, "提示", '请测试车检器')
            self.speaker.speak("请将线圈靠近磁铁")
            self.__manulAskDlg('提示', "请将线圈靠近磁铁")

    @pyqtSlot()
    def on_key2_clicked(self):
        self.key2.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.gpio = GPIO(self)
        if  self.gpio.isRunning:
             self.key2.setDisabled(True)
             start_new_thread(self.gpio.Inlevel_Down, (CFG["key2"][0],))
            # start_new_thread(self.setOutTime, ("Print", 10))
             QtGui.QMessageBox.about(self, "提示", '请测试微动开关')

    @pyqtSlot()
    def on_key3_clicked(self):
        self.key3.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.MicroKey = GPIO(self)
        if self.MicroKey.isRunning:
            self.key3.setDisabled(True)
            start_new_thread(self.MicroKey.Inlevel, (CFG["key3"][0],))
            # start_new_thread(self.setOutTime, ("MicroKey", 10))
            QtGui.QMessageBox.about(self, "提示", '请按下呼叫开关')

    @pyqtSlot()
    def on_key4_clicked(self):
        self.key4.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.CarTest = GPIO(self)
        if self.CarTest.isRunning:
            self.key4.setDisabled(True)
            start_new_thread(self.CarTest.Inlevel, (CFG["key4"][0],))
            # start_new_thread(self.setOutTime, ("CarTest", 10))
            QtGui.QMessageBox.about(self, "提示", '请按下打印按键')

    def __GPIOKeyConfirm(self, pinnum, status):
        '''GPIO按键状态确认'''
        key = 'key' + str(pinnum)
        if status == "true":
            self.__dict__[key].setStyleSheet("background-color:green")
            self.logUi.log('%s测试正常' % CFG[key][1])
        #    Speaker.speak('%s测试正常' % CFG[key][1])
        else:
            self.__dict__[key].setStyleSheet("background-color:red")
            self.logUi.log('%s测试不通过' % CFG[key][1])
         #   Speaker.speak('%d测试不通过' % CFG[key][1])
        self.__dict__[key].setDisabled(False)


    @pyqtSlot()
    def on_out1_clicked(self):
        self.out1.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.testGPIO_O(CFG["out1"][0],self.out1,"out1")


    @pyqtSlot()
    def on_out2_clicked(self):
        self.out1.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.testGPIO_O(CFG["out2"][0],self.out2,"out2")

    @pyqtSlot()
    def on_out3_clicked(self):
        self.out1.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.testGPIO_O(CFG["out3"][0],self.out3,"out3")

    @pyqtSlot()
    def on_out4_clicked(self):
        self.out1.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.testGPIO_O(CFG["out4"][0],self.out4,"out4")


    def testGPIO_O(self,pin,outNo,no):
        gpio = GPIO(self)
        if gpio.isRunning:
            outNo.setDisabled(True)
            start_new_thread(gpio.test, (CFG[no][0],))
            outNo.setDisabled(False)


    def __OutConfirm(self, pinnum):
        '''GPIO输出状态设置'''
        pin = "out" + str(pinnum - 5)
        rst = QtGui.QMessageBox.warning(self, "确认", '请确认灯带是否灭过', '正确', '错误')
        if rst == 0:
            self.__dict__[pin].setStyleSheet("background-color:green")
            self.logUi.log('%s测试正常' % CFG[pin][1])
            Speaker.speak('%s测试正常' % (CFG[pin][1]))

        else:
            self.__dict__[pin].setStyleSheet("background-color:red")
            self.logUi.log('%s不通过' % CFG[pin][1])
          #  Speaker.speak('%s测试不通过' % CFG[pin][1])

        self.key1.setDisabled(False)


    @pyqtSlot()
    def on_PrinterCM_clicked(self):
        self.printerMC = Printer(self)
        start_new_thread(self.printer.copyMechine,('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '线上支付', '2019-3-24-10:30:45',
                          '2019-3-24-1:30:51', 'http://www.baidu.com'))

    @pyqtSlot()
    def on_ScannerMC_clicked(self):
        self.scannerMC = ScannerInterface(9600,self)
        start_new_thread(self.scannerMC.copyMechine,())

    # @pyqtSlot()
    # def on_GPO_clicked(self):
    #     self.GPOMC = GPIO(self)
    #     start_new_thread(self.GPOMC.copyMechine,(pin,))
    @pyqtSlot()
    def on_stopMC_clicked(self):
        if self.scannerMC != None:self.scannerMC.isRunning = False
        if  self.casherMC != None:self.casherMC. isRunning = False
        if  self.printerMC!= None: self.printerMC.isRunning = False
        if self.GPOMC1 != None:self.GPOMC1.isRunning = False
        if self.music!=None:self.music.isRunning = False

    @pyqtSlot()
    def on_QuickMC_clicked(self):
        self.printerMC = Printer(self)
        if self.printerMC.port:
            start_new_thread(self.printerMC.copyMechine,
                             ('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '线上支付', '2019-3-24-10:30:45',
                              '2019-3-24-1:30:51', 'http://www.baidu.com'))
        if isEntry == 'False' :
            self.scannerMC = ScannerInterface(9600, self)
            if self.scannerMC.port:
                start_new_thread(self.scannerMC.copyMechine, ())
            else:
                self.logUi.log("找不到扫码枪串口，请检查连线！")
            self.casherMC = Casher(CFG['casherCom'], self)
            if self.casherMC.isopen == 1:
                start_new_thread(self.casherMC.copyMC,())
            else:
                self.logUi.log("吃钞票机连接失败，请检查连线！")
        self.GPOMC1 = GPIO(self)
        if self.GPOMC1.isRunning:
            start_new_thread(self.GPOMC1.copyMechine, (CFG['out1'][0],))
            start_new_thread(self.GPOMC1.copyMechine, (CFG['out2'][0],))
            start_new_thread(self.GPOMC1.copyMechine, (CFG['out4'][0],))
        self.music=Music()
        start_new_thread(self.music.play,(CFG['mp3'],))



    @pyqtSlot()
    def on_RstBtn_clicked(self):
        self.voiceBtn.setText('未测试')
        self.voiceBtn.setStyleSheet("background-color: rgb(86,86,86)")

        self.PrinterStatus.setText('未测试')
        self.PrinterStatus.setStyleSheet("background-color: rgb(86, 86, 86)")

        self.Casherstatus = [-1, -1, -1]
        self.CasherStatus.setText('未测试')
        self.CasherStatus.setStyleSheet("background-color: rgb(86, 86, 86)")

        self.Scanstatus.setText('未测试')
        self.Scanstatus.setStyleSheet("background-color: rgb(86, 86, 86)")

        for i in range(1, 5):
            key = "key" + str(i)
            out = "out" + str(i)
            self.__dict__[key].setStyleSheet("background-color: rgb(86, 86, 86)")
            self.__dict__[out].setStyleSheet("background-color: rgb(86, 86, 86)")

        # self.RMB5Test.setText('未测试')
        self.RMB5Test.setDisabled(False)
        self.RMB5Test.setStyleSheet("background-color: rgb(86, 86, 86)")
        # self.RMB10Test.setText('未测试')
        self.RMB10Test.setDisabled(False)
        self.RMB10Test.setStyleSheet("background-color: rgb(86, 86, 86)")

        self.ErrTestBtn.setDisabled(False)
        self.ErrTestBtn.setStyleSheet("background-color: rgb(86, 86, 86)")

        # self.logUi.clear()
        self.SanInfo.setText('')

    def __manulAskDlg(self, title, msg):
        self.confirmDlg = QtGui.QMessageBox()
        self.confirmDlg.setWindowTitle(title)
        self.confirmDlg.setIcon(QtGui.QMessageBox.Information)
        self.confirmDlg.setText(msg)
        self.confirmDlg.setParent(self)
        self.confirmDlg.setWindowFlags(QtCore.Qt.Dialog)
        self.confirmDlg.addButton("确定", QtGui.QMessageBox.AcceptRole)

        self.manulDlgResult = self.confirmDlg.exec_()

    def __manulAskDlgTrigger(self, result):
        if result == "NORMAL":
            self.confirmDlg.done(0)
        elif result == "ABNORMAL":
            self.confirmDlg.done(1)


class LogUi:
    '''日志框'''

    def __init__(self, logListView):
        self.logListView = logListView
        self.qi = QtGui.QStandardItemModel()
        logListView.setModel(self.qi)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        fh = logging.handlers.RotatingFileHandler(str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+'.log', maxBytes=1024 * 1024 * 10, backupCount=5,
                                                  encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        ch.setFormatter(Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'))
        fh.setFormatter(Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'))

    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def log(self, message):

        logMessage = LogUi.now() + "\t" + message
        logItem = QtGui.QStandardItem(logMessage)
        if '失败' in message or '不通过' in message or '离线' in message or '超时' in message or '异常' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.red))
            self.logger.error(message)
        elif '终止' in message or '关闭' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.blue))
            self.logger.warning(message)
        elif '成功' in message or '正常' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.green))
            self.logger.info(message)
        else:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.gray))
            self.logger.debug(message)

        logItem.setEditable(False)
        self.qi.appendRow(logItem)
        if self.qi.rowCount() >= 100:
            self.qi.removeRow(0)
        self.logListView.scrollToBottom()
