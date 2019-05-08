# encoding:utf-8
"""
模块:

@author:zws
"""
import time
from ctypes import *
from ctypes.wintypes import *

hComContext = HANDLE()
dwSysErr = DWORD()
dwStatus = DWORD()

import json
import random

CFG = json.load(open('config.json', 'r', encoding='utf-8'))


class Printer:

    def __init__(self, ui):
        self.dll = cdll.LoadLibrary("CePrnLib.dll")
        self.ui = ui
        if self.openCom(CFG["printerCom"]):
            self.ui.logUi.log('正在启动打印机')
            self.set_com()
            self.port = True
            self.isRunning = True
        else:
            self.port = None
            self.ui.logUi.log('打印机启动失败，请检查是否正确连接')
            self.isRunning = False

    def openCom(self, com):
        # 打开串口
        rtn = self.dll.CeOpenCom(byref(hComContext), com, byref(dwSysErr))
        print("open serial:", rtn, hComContext, dwSysErr.value)
        return True if rtn == 0 else False

    def closeCom(self):
        # 关闭串口
        rtn = self.dll.CeCloseCom(hComContext)
        print("close serial:", rtn, hComContext, dwSysErr.value)
        return True if rtn == 0 else False

    def set_com(self):
        # 设置串口
        dwCodedErr = self.dll.CeSetComCfgHR(hComContext, 115200, 0, 8, 0, 1, byref(dwSysErr))
        print("set serial:", hComContext, dwSysErr.value)

    # def generateQBar(self, value):
    #     # 生成二维码
    #     import qrcode
    #     qr = qrcode.QRCode(version=1,
    #                        error_correction=qrcode.constants.ERROR_CORRECT_L,
    #                        box_size=5,
    #                        border=2)
    #     qr.add_data(value)
    #     qr.make(fit=True)
    #     img = qr.make_image()
    #     img = img.convert("1")
    #     img.save("qb.bmp")

    def printRaw(self, title, car_info, H_M_S, cost, real_cost, change, voucher, type, in_time, out_time, codebar):
        '''

        :param title: 小票标题
        :param car_info: 车牌号
        :param H_M_S: 停车时长
        :param cost: 花费
        :param real_cost:实际缴费  float
        :param change: 找零
        :param voucher:优惠券有无
        :param type: 交易类型
        :param in_time:入场时间
        :param in_time:出场时间
        :param codebar: 二维码信息  现金支付无找零时打印公众号
        :return:
        '''

        # 校准
        try:
            res = self.checkOutOfPaper()
            noPaper = (res >> 24) & 0x01
            nearPaper = res >> 26 & 0x01
            if noPaper == 1:
                self.ui.emit(self.ui.LOGPRINT, "-*************打印失败，打印机没纸,请检查！")
                self.ui.emit(self.ui.PRINTSTATUS, True)
            else:
                if nearPaper == 1:
                    self.ui.emit(self.ui.LOGPRINT, "*************打印机即将没纸,请注意检查！")
                rtn = self.dll.CeSetJustification(hComContext, 0x01, byref(dwSysErr))
                print("center justy:", rtn, dwSysErr.value)

                # 设置文本格式
                rtn = self.dll.CeSetTextMode(hComContext, 0x00, byref(dwSysErr))
                print("setTextMode:", rtn, dwSysErr.value)

                # 走纸
                # rtn = dll.CeLF(hComContext, 1, byref(dwSysErr))
                # print("lf:", rtn, dwSysErr.value)

                # 打印
                textBuffer = create_string_buffer(32)
                title = "%s停车场凭条" % (title)
                txtBytes = title.encode('gbk')  # 编码成gbk
                rtn = self.dll.CeWriteTxt(hComContext, txtBytes, byref(dwSysErr))

                # 走纸
                rtn = self.dll.CeLF(hComContext, 1, byref(dwSysErr))
                if type == "现金支付":
                    toPrintTexts = [
                        "   车牌号    %s" % (car_info) + ' ' * 6 + '停车时长  ' + '%s\0' % (H_M_S),
                        "   应收金额  %.2f元" % (cost) + ' ' * (len(car_info) - len(str(cost)) + 4) + '实收金额  ' + '%.2f元\0' % (
                            real_cost),
                        "   找零金额  %.2f元" % (change) + ' ' * (
                                    len(car_info) - len(str(change)) + 4) + "优惠券   " + '%s' % voucher,
                        "   缴费方式  %s\0" % (type),
                        "   入场时间  %s\0" % in_time,
                        "   出场时间  %s\0" % out_time
                    ]
                else:
                    toPrintTexts = [
                        "   车牌号    %s" % (car_info) + ' ' * 6 + '停车时长  ' + '%s\0' % (H_M_S),
                        "   缴费金额  %.2f元" % (cost) + ' ' * (len(car_info) - len(str(cost)) + 4) + "优惠券   " + '%s' % voucher,
                        "   缴费方式  %s\0" % (type),
                        "   入场时间  %s\0" % in_time,
                        "   出场时间  %s\0" % out_time
                    ]

                # 校准
                rtn = self.dll.CeSetJustification(hComContext, 0x00, byref(dwSysErr))
                print("center justy:", rtn, dwSysErr.value)

                for txt in toPrintTexts:
                    txtBytes = txt.encode("gbk")
                    # textBuffer.raw = txt.encode('utf-8')
                    rtn = self.dll.CeWriteTxt(hComContext, txtBytes, byref(dwSysErr))
                    print("print:", rtn, dwSysErr.value)

                # 校准
                rtn = self.dll.CeSetJustification(hComContext, 0x01, byref(dwSysErr))
                print("center justy:", rtn, dwSysErr.value)

                # 打印二维码  如果是现金支付且需要找零二维码是零钱，否则是公众号
                #  self.generateQBar(codebar)
                strFilePath = "qb.bmp"
                self.dll.CePrintRasterImage(hComContext, strFilePath, 0, byref(dwSysErr))

                # 走纸
                rtn = self.dll.CeLF(hComContext, 1, byref(dwSysErr))
                if type == "现金支付" and change != 0:
                    txtBytes = "提示：请在24小时之内扫码找零，超时二维码即将过期".encode('gbk')
                elif type == "线上支付":
                    txtBytes = "关注老友泊车公众号,获取最新优惠活动".encode('gbk')
                rtn = self.dll.CeWriteTxt(hComContext, txtBytes, byref(dwSysErr))

                # 走纸
                # rtn = dll.CeLF(hComContext, 1, byref(dwSysErr))
                # print("lf:", rtn, dwSysErr.value)
                #
                # 切
                rtn = self.dll.CePCut(hComContext, byref(dwSysErr))
                print("cut:", rtn, dwSysErr.value)
                self.ui.emit(self.ui.PRINTSTATUS, False)
                time.sleep(1)  # 如果关闭串口过快会导致切纸没有执行
            self.closeCom()
        except Exception as e:
            print(e)
            self.ui.emit(self.ui.LOGPRINT, "打印机异常，请检查连线！")
            self.ui.emit(self.ui.PRINTSTATUS, True)
            self.closeCom()


    def isNoPaper(self):
        rtn = self.dll.CeGetSts(hComContext, byref(dwStatus), byref(dwSysErr))
        return (dwStatus.value >> 24) & 0x01

    def checkOutOfPaper(self):
        # 打印机是否缺纸，缺纸返回True
        # pass
        # 获取状态  希望以此查看打印机是否与缺纸 还未完善
        rtn = self.dll.CeGetSts(hComContext, byref(dwStatus), byref(dwSysErr))

        print("status:", rtn, dwStatus.value, dwSysErr.value)
        return dwStatus.value

    def copyMechine(self, title, car_info, H_M_S, cost, real_cost, change, voucher, type, in_time, out_time, codebar):
        '''
        :param title: 小票标题
        :param car_info: 车牌号
        :param H_M_S: 停车时长
        :param cost: 花费
        :param real_cost:实际缴费  float
        :param change: 找零
        :param voucher:优惠券有无
        :param type: 交易类型
        :param in_time:入场时间
        :param in_time:出场时间
        :param codebar: 二维码信息  现金支付无找零时打印公众号
        :return:
        '''
        successNo = 0
   #     try:
            # 校准
        rtn = self.dll.CeSetJustification(hComContext, 0x01, byref(dwSysErr))
        # 设置文本格式
        rtn = self.dll.CeSetTextMode(hComContext, 0x00, byref(dwSysErr))
        # 打印
        titleAll = "%s停车场凭条" % (title)
        titleBytes = titleAll.encode('gbk')  # 编码成gbk
        if type == "现金支付":
            toPrintTexts = [
                "   车牌号    %s" % (car_info) + ' ' * 6 + '停车时长  ' + '%s\0' % (H_M_S),
                "   应收金额  %.2f元" % (cost) + ' ' * (
                        len(car_info) - len(str(cost)) + 4) + '实收金额  ' + '%.2f元\0' % (
                    real_cost),
                "   找零金额  %.2f元" % (change) + ' ' * (
                        len(car_info) - len(str(change)) + 4) + "优惠券   " + '%s' % voucher,
                "   缴费方式  %s\0" % (type),
                "   入场时间  %s\0" % in_time,
                "   出场时间  %s\0" % out_time
            ]
        else:
            toPrintTexts = [
                "   车牌号    %s" % (car_info) + ' ' * 6 + '停车时长  ' + '%s\0' % (H_M_S),
                "   缴费金额  %.2f元" % (cost) + ' ' * (
                        len(car_info) - len(str(cost)) + 4) + "优惠券   " + '%s' % voucher,
                "   缴费方式  %s\0" % (type),
                "   入场时间  %s\0" % in_time,
                "   出场时间  %s\0" % out_time
            ]

        strFilePath = "qb.bmp"
        while self.isRunning:
            try:
                if self.isNoPaper():
                    self.ui.emit(self.ui.LOGPRINT, "----------打印机没纸，请检查！！----------------")
                    time.sleep(10)
                else:
                    rtn = self.dll.CeWriteTxt(hComContext, titleBytes, byref(dwSysErr))
                    # 走纸
                    rtn = self.dll.CeLF(hComContext, 1, byref(dwSysErr))
                    # 校准
                    rtn = self.dll.CeSetJustification(hComContext, 0x00, byref(dwSysErr))
                    for txt in toPrintTexts:
                        txtByte = txt.encode("gbk")
                        rtn = self.dll.CeWriteTxt(hComContext, txtByte, byref(dwSysErr))
                    # 校准
                    rtn = self.dll.CeSetJustification(hComContext, 0x01, byref(dwSysErr))
                    # 打印二维码  如果是现金支付且需要找零二维码是零钱，否则是公众号
                    self.dll.CePrintRasterImage(hComContext, strFilePath, 0, byref(dwSysErr))
                    # 走纸
                    rtn = self.dll.CeLF(hComContext, 1, byref(dwSysErr))
                    if type == "现金支付" and change != 0:
                        txtBytes = "提示：请在24小时之内扫码找零，超时二维码即将过期".encode('gbk')
                    elif type == "线上支付":
                        txtBytes = "关注老友泊车公众号,获取最新优惠活动".encode('gbk')
                    rtn = self.dll.CeWriteTxt(hComContext, txtBytes, byref(dwSysErr))
                    # 切
                    rtn = self.dll.CePCut(hComContext, byref(dwSysErr))
                    print("cut:", rtn, dwSysErr.value)
                    successNo += 1
                    self.ui.emit(self.ui.LOGPRINT, "----------打印成功，次数：" + str(successNo))
                    time.sleep(random.randint(1, 10))  # 如果关闭串口过快会导致切纸没有执行
            except Exception as e:
                #  time.sleep(60 * 3)
                self.ui.logUi.log('打印机异常')
                if self.port == False:
                    self.openCom(CFG["printerCom"])

        self.closeCom()
        self.ui.emit(self.ui.LOGPRINT, "----------打印机已关闭----------------")
        time.sleep(60*2)

if __name__ == '__main__':
    printer = Printer('com3')
    printer.printRaw('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '线上支付', '2019-3-24-10:30:45',
                     '2019-3-24-1:30:51', 'http://www.baidu.com')
    # printer.printRaw('天津国际机场', '津Q45689', '3小时20分45秒', 12.6, 15, 2.4, '无', '现金支付', '2019-3-24-10:30:45',
    #                  '2019-3-24-1:30:51', '找零2.4元')
