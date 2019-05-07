# encoding:utf-8
"""
GPIO测试工具
@author:zws
"""
import time

import pywinio



class GPIO:
    pinAddMap = {6: (0xa02, 5), 7: (0xa03, 7), 8: (0xa05, 4), 9: (0xa05, 5)}

    def __init__(self,ui):
        try:
            self.ui = ui
            self.isRunning = True
            self.wio = pywinio.WinIO()
        except Exception as e:
            self.ui.logUi.log('GPIO 启动失败！')
            self.isRunning = False



    def read(self,pinnum):
        # input("press ENTER to read status")
        vA00 = self.wio.get_port_byte(0xA00)
        vA02 = self.wio.get_port_byte(0xA02)

        pin1Value = vA00 & (0b01 << 1) != 0
        pin2Value = vA00 & (0b01 << 5) != 0
        pin3Value = vA00 & (0b01 << 6) != 0
        pin4Value = vA02 & (0b01 << 3) != 0

        # print("pin1:%d\tpin2:%d\tpin3:%d\tpin4:%d" % (pin1Value, pin2Value, pin3Value, pin4Value))
        status = [pin1Value, pin2Value, pin3Value, pin4Value]
        return int(status[pinnum - 1])




    def write(self,pin,v):

        currentValue = self.wio.get_port_byte(self.pinAddMap[pin][0])

        if v == 0:
            currentValue &= (~(0b01 << self.pinAddMap[pin][1]))
        else:
            currentValue |= (0b01 << self.pinAddMap[pin][1])

        self.wio.set_port_byte(self.pinAddMap[pin][0], currentValue)
        


    def Inlevel(self,pin):
        change = [0,0,0]
        v = self.read(pin)
        change[0] = v
        while change[0]  and self.isRunning:
            time.sleep(0.1)
            v = self.read(pin)
            while v==0 and self.isRunning:
                change[1]=0
                time.sleep(0.1)
                v = self.read(pin)
                while v==1 and self.isRunning:
                    change[2]=1
                    self.ui.emit(self.ui.LEVELCHANGE,pin,'true')
                    return True
        self.ui.emit(self.ui.LEVELCHANGE, pin,'false')
        return False


    def Inlevel_Down(self,pin):
        change = [0, 0]
        v = self.read(pin)
        change[0] = v
        while change[0] and self.isRunning:
            time.sleep(0.5)
            v = self.read(pin)
            while v == 0 and self.isRunning:
                change[1] = 0
                time.sleep(0.5)
               # v = self.read(pin)
                self.ui.emit(self.ui.LEVELCHANGE, pin, 'true')
                return True
        self.ui.emit(self.ui.LEVELCHANGE, pin, 'false')
        return False

    def test(self,pin):
        for i in range(1,4):
            self.write(pin,0)
            time.sleep(0.5)
            self.write(pin,1)
            time.sleep(0.5)

        self.ui.emit(self.ui.OUT, pin)

    def copyMechine(self,pin):
        while self.isRunning:
            self.write(pin,0)
            time.sleep(0.5)
            self.write(pin,1)
            time.sleep(0.5)

