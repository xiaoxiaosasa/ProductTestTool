# -*- coding: UTF-8 -*-
# author:yuliang

import time

import serial
from DeviceTest.voice import Speaker

import json
import random

CFG = json.load(open('config.json', 'r', encoding='utf-8'))


class ScannerInterface():
    def __init__(self, baudrate, ui):
        self.port = None  # 串口
        self.baudrate = baudrate  # 波特率
        self.ui = ui
        self.serial = None  # 串口句柄
        self.__findCom()
        self.suceessNo = 0

        if self.port:
            self.PortInit(self.port)  # 串口初始化
            self.isRunning = True
        else:
            self.ui.logUi.log('扫码枪连接失败，请插入扫码枪')
            self.isRunning = False

    def __findCom(self):

        import serial.tools.list_ports

        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            print('找不到串口')
        else:
            for i in range(0, len(port_list)):
                portInfo = str(port_list[i])
                if "[online] Newland NLS-FM430-ER" in portInfo:  # ？
                    port = portInfo[-5:-1]
                    print(port)
                    self.port = port
                    break

    def PortInit(self, port):
        '''开启扫描仪对应的串口'''
        try:
            self.serial = serial.Serial(self.port, baudrate=self.baudrate, timeout=1,
                                        parity=serial.PARITY_EVEN, rtscts=1)
            self.ui.logUi.log('正在启动扫码枪')
        except Exception as e:
            print('open error:', e)
            self.ui.logUi.log('扫码枪启动失败，请检查是否正确连接')
            self.isRunning = False

    def recv_rst(self):
        '''接收数据'''
        while True:
            if self.isRunning == False:
                self.PortInit(self.port)
            try:
                if self.serial and self.serial.in_waiting:
                    # info = self.serial.read(self.serial.in_waiting).decode('utf-8') 如果是中文,解码
                    self.info = self.serial.read(self.serial.in_waiting)

                    if b"NG" not in self.info and b'\x06' not in self.info:
                        # 读取二维码成功
                        # print("收到数据：", str(info), type(str(info)))
                        info = str(self.info)

                        print(info.split('\'')[1].split('\\')[0])
                        result = info.split('\'')[1].split('\\')[0]
                        self.ui.logUi.log("扫码：%s" % (result))
            except Exception as e:
                print('send:', e)
                #  self.serial.close()
                self.isRunning = False

    def scan(self, isOnce):
        t = 0
        while t < CFG['TIMEOUT']:
            try:
                if self.serial and self.serial.in_waiting:
                    # info = self.serial.read(self.serial.in_waiting).decode('utf-8') 如果是中文,解码
                    self.info = self.serial.read(self.serial.in_waiting)
                    if (b"NG" in self.info):  # 退出标志
                        continue
                    elif b'\x06' in self.info:
                        continue
                    else:
                        # 读取二维码成功
                        # print("收到数据：", str(info), type(str(info)))
                        result = str(self.info).split('\'')[1].split('\\')[0]
                        self.suceessNo += 1
                        msg = "##########扫码成功，次数：" + str(self.suceessNo)
                        self.ui.emit(self.ui.LOGPRINT, msg)
                        if isOnce:
                            self.ui.emit(self.ui.SCANNERSTATUS, result)
                        t = 0
                        break
                time.sleep(0.5)
                t += 0.5
                if t >= CFG['TIMEOUT']:
                    msg = "扫码枪等待扫码超时..."
                    self.ui.emit(self.ui.LOGPRINT, msg)
                    if isOnce:
                        self.ui.emit(self.ui.SCANNERSTATUS, "")
                continue
            except Exception as e:
                print('send:', e)
                self.ui.logUi.log('扫码枪异常')
                self.serial.close()
                # self.isRunning = False
                break

    def set_scanner(self, pram):
        if self.serial.isOpen() == False:
            self.PortInit(self.port)
        result = self.serial.write(pram)  # 设置扫描仪
        # print('设置命令字节数:', result)

    def startScanning(self):
        self.set_scanner(b'\x1b\x31')  # 模拟按键触发
        print('开始扫码')

    def stopScanning(self):
        self.set_scanner(b'\x1b\x30')  # 模拟按键松开
        print('结束扫码')

    def close(self):
        self.serial.close()  # 关闭串口
        self.ui.emit(self.ui.LOGPRINT, "扫码枪串口关闭！")
        self.isRunning = False

    def test(self):
        self.startScanning()
        param = self.scan(True)
        self.stopScanning()
        self.close()

    # self.ui.emit(self.ui.SCANNERSTATUS,param)

    def copyMechine(self):
        while self.isRunning:
            if self.serial.isOpen() == False:
                self.PortInit(self.port)
            self.startScanning()
            self.scan(False)
            self.stopScanning()
            time.sleep(1)
        self.stopScanning()
        self.close()


if __name__ == '__main__':
    scan = ScannerInterface("com4", 9600)  # 串口默认波特率9600，在程序中9600、38400都可以，但在张总的串口中必须为38400

    # scan.set_scanner(b'\x1b\x32')  # 模拟按键触发
    # scan.recv_rst()  # 接收扫描数据，如果接收为NG继续接收直到扫描成功，期间不需要按扫描仪，只需要对准二维码
    # scan.set_scanner(b'\x1b\x30')  # 模拟按键松开
    # scan.recv_rst()
    # time.sleep(5)
    # scan.close()
    scan.startScanning()
    scan.scan()
    scan.stopScanning()
