# encoding:utf-8
"""
模块:

@author:zws
"""

from ctypes import *

import time

SSP_CMD_RESET = 0x01
SSP_CMD_HOST_PROTOCOL_VERSION = 0x06
SSP_CMD_SYNC = 0x11
SSP_CMD_SET_GENERATOR = 0x4A
SSP_CMD_SET_MODULUS = 0x4B
SSP_CMD_KEY_EXCHANGE = 0x4C
SSP_CMD_SET_INHIBITS = 0x02
SSP_CMD_ENABLE = 0x0A
SSP_CMD_DISABLE = 0x09
SSP_CMD_POLL = 0x07
SSP_CMD_SETUP_REQUEST = 0x05
SSP_CMD_DISPLAY_ON = 0x03
SSP_CMD_DISPLAY_OFF = 0x04
SSP_CMD_ENABLE_PAYOUT = 0x5C
SSP_CMD_DISABLE_PAYOUT = 0x5B
SSP_CMD_SET_ROUTING = 0x3B
SSP_CMD_SET_VALUE_REPORTING_TYPE = 0x45
SSP_CMD_PAYOUT_LAST_NOTE = 0x42
SSP_CMD_EMPTY = 0x3F
SSP_CMD_GET_NOTE_POSITIONS = 0x41
SSP_CMD_STACK_LAST_NOTE = 0x43
SSP_CMD_LAST_REJECT_CODE = 0x17

SSP_POLL_RESET = 0xF1
SSP_POLL_NOTE_READ = 0xEF
SSP_POLL_CREDIT = 0xEE
SSP_POLL_REJECTING = 0xED
SSP_POLL_REJECTED = 0xEC
SSP_POLL_STACKING = 0xCC
SSP_POLL_STACKED = 0xEB
SSP_POLL_SAFE_JAM = 0xEA
SSP_POLL_UNSAFE_JAM = 0xE9
SSP_POLL_DISABLED = 0xE8
SSP_POLL_FRAUD_ATTEMPT = 0xE6
SSP_POLL_STACKER_FULL = 0xE7
SSP_POLL_NOTE_CLEARED_FROM_FRONT = 0xE1
SSP_POLL_NOTE_CLEARED_TO_CASHBOX = 0xE2
SSP_POLL_CASHBOX_REMOVED = 0xE3
SSP_POLL_CASHBOX_REPLACED = 0xE4
SSP_POLL_BARCODE_TICKET_VALIDATED = 0xE5
SSP_POLL_BARCODE_TICKET_ACK = 0xD1
SSP_POLL_NOTE_PATH_OPEN = 0xE0
SSP_POLL_CHANNEL_DISABLE = 0xB5
SSP_POLL_INITIALISING = 0xB6

SSP_RESPONSE_CMD_OK = 0xF0
SSP_RESPONSE_CMD_UNKNOWN = 0xF2
SSP_RESPONSE_CMD_WRONG_PARAMS = 0xF3
SSP_RESPONSE_CMD_PARAM_OUT_OF_RANGE = 0xF4
SSP_RESPONSE_CMD_CANNOT_PROCESS = 0xF5
SSP_RESPONSE_CMD_SOFTWARE_ERROR = 0xF6
SSP_RESPONSE_CMD_FAIL = 0xF8
SSP_RESPONSE_CMD_KEY_NOT_SET = 0xFA


class SSP_FULL_KEY(Structure):
    _fields_ = [
        ("FixedKey", c_ulonglong),
        ("EncryptKey", c_ulonglong),
    ]


class SSP_COMMAND(Structure):
    _fields_ = [
        ("Key", SSP_FULL_KEY),
        ("BaudRate", c_ulong),
        ("Timeout", c_ulong),

        ("PortNumber", c_ubyte),
        ("SSPAddress", c_ubyte),
        ("RetryLevel", c_ubyte),
        ("EncryptionStatus", c_ubyte),
        ("CommandDataLength", c_ubyte),

        ("CommandData", c_ubyte * 255),
        ("ResponseStatus", c_ubyte),
        ("ResponseDataLength", c_ubyte),
        ("ResponseData", c_ubyte * 255),
        ("IgnoreError", c_ubyte),
    ]


class SSP_PACKET(Structure):
    _fields_ = [
        ("packetTime", c_ushort),
        ("PacketLength", c_ubyte),
        ("PacketData", c_ubyte * 255)
    ]


class SSP_COMMAND_INFO(Structure):
    _fields_ = [
        ("CommandName", c_char_p),
        ("LogFileName", c_char_p),
        ("Encrypted", c_ubyte),
        ("Transmit", SSP_PACKET),
        ("Receive", SSP_PACKET),
        ("PreEncryptTransmit", SSP_PACKET),
        ("PreEncryptRecieve", SSP_PACKET),
    ]


class SSP_KEYS(Structure):
    _fields_ = [
        ("Generator", c_uint64),
        ("Modulus", c_uint64),
        ("HostInter", c_uint64),
        ("HostRandom", c_uint64),
        ("SlaveInterKey", c_uint64),
        ("SlaveRandom", c_uint64),
        ("KeyHost", c_uint64),
        ("KeySlave", c_uint64)
    ]


class SSP_CONNECTION_INFO(Structure):
    _fields_ = [
        ("Port", c_char_p),
        ("SSPAddress", c_char),
        ("ProtocolVersion", c_char),
        ("RetryLevel", c_char),
        ("BaudRate", c_long),
        ("TimeOut", c_long)

    ]


CMD_NAMES = {
    0x4A: b"SET GENERATOR",
    0x4B: b"SET MODULUS",
    0x4C: b"REQUEST KEY EXCHANGE",
    0x01: b"RESET",
    0x02: b"SET INHIBITS",
    0x03: b"DISPLAY ON",
    0x04: b"DISPLAY OFF",
    0x05: b"SETUP REQUEST",
    0x06: b"HOST PROTOCOL VERSION",
    0x07: b"POLL",
    0x08: b"REJECT",
    0x09: b"DISABLE",
    0x0A: b"ENABLE",
    0x0B: b"PROGRAM FIRMWARE",
    0x0C: b"GET SERIAL NUMBER",
    0x0D: b"UNIT DATA",
    0x0E: b"CHANNEL VALUE DATA",
    0x0F: b"CHANNEL SECURITY DATA",
    0x10: b"CHANNEL RETEACH DATA",
    0x11: b"SYNC",
    0x12: b"UPDATE COIN ROUTE",
    0x13: b"DISPENSE",
    0x14: b"HOST SERIAL NUMBER REQUEST",
    0x15: b"SETUP REQUEST",
    0x17: b"LAST REJECT CODE",
    0x18: b"HOLD",
    0x19: b"ENABLE PROTOCOL VERSION EVENTS",
    0x23: b"GET BAR CODE READER CONFIGURATION",
    0x24: b"SET BAR CODE READER CONFIGURATION",
    0x25: b"GET BAR CODE INHIBIT",
    0x26: b"SET BAR CODE INHIBIT",
    0x27: b"GET BAR CODE DATA",
    0x54: b"CONFIGURE BEZEL",
    0x56: b"POLL WITH ACK",
    0x57: b"EVENT ACK",
    0x3B: b"SET ROUTING",
    0x3C: b"GET ROUTING",
    0x33: b"PAYOUT AMOUNT",
    0x35: b"GET NOTE/COIN AMOUNT",
    0x34: b"SET NOTE/COIN AMOUNT",
    0x38: b"HALT PAYOUT",
    0x3D: b"FLOAT AMOUNT",
    0x3E: b"GET MINIMUM PAYOUT",
    0x40: b"SET COIN MECH INHIBITS",
    0x46: b"PAYOUT BY DENOMINATION",
    0x44: b"FLOAT BY DENOMINATION",
    0x47: b"SET COMMAND CALIBRATION",
    0x48: b"RUN COMMAND CALIBRATION",
    0x3F: b"EMPTY ALL",
    0x50: b"SET OPTIONS",
    0x51: b"GET OPTIONS",
    0x49: b"COIN MECH GLOBAL INHIBIT",
    0x52: b"SMART EMPTY",
    0x53: b"CASHBOX PAYOUT OPERATION DATA",
    0x5C: b"ENABLE PAYOUT DEVICE",
    0x5B: b"DISABLE PAYOUT DEVICE",
    0x58: b"GET NOTE COUNTERS",
    0x59: b"RESET NOTE COUNTERS",
    0x30: b"SET REFILL MODE",
    0x41: b"GET NOTE POSITIONS",
    0x42: b"PAYOUT NOTE",
    0x43: b"STACK NOTE",
    0x45: b"SET VALUE REPORTING TYPE"
}

dll = windll.LoadLibrary("ITLSSPProc.dll")

commandStructure = SSP_COMMAND()
commandStructure.BaudRate = 9600
commandStructure.Timeout = 1000
commandStructure.RetryLevel = 3
commandStructure.IgnoreError = 1
commandStructure.SSPAddress = 0

info = SSP_COMMAND_INFO()

money = {
    1: 1,
    2: 5,
    3: 10,
    4: 20,
    5: 50,
    6: 100
}

total = 0  # total 代表总金额

RESPONSE_NAMES = {
    SSP_RESPONSE_CMD_OK: "OK",

    SSP_RESPONSE_CMD_CANNOT_PROCESS: "Command response is CANNOT PROCESS COMMAND",
    SSP_RESPONSE_CMD_FAIL: "Command response is FAIL",
    SSP_RESPONSE_CMD_KEY_NOT_SET: "Command response is KEY NOT SET, renegotiate keys",
    SSP_RESPONSE_CMD_PARAM_OUT_OF_RANGE: "Command response is PARAM OUT OF RANGE",
    SSP_RESPONSE_CMD_SOFTWARE_ERROR: "Command response is SOFTWARE ERROR",
    SSP_RESPONSE_CMD_UNKNOWN: "Command response is UNKNOWN",
    SSP_RESPONSE_CMD_WRONG_PARAMS: "Command response is WRONG PARAMETERS",

    SSP_POLL_RESET: "SSP_POLL_RESET",
    SSP_POLL_NOTE_READ: "SSP_POLL_NOTE_READ",
    SSP_POLL_CREDIT: "SSP_POLL_CREDIT",
    SSP_POLL_REJECTING: "SSP_POLL_REJECTING",
    SSP_POLL_REJECTED: "SSP_POLL_REJECTED",
    SSP_POLL_STACKING: "SSP_POLL_STACKING",
    SSP_POLL_STACKED: "SSP_POLL_STACKED",
    SSP_POLL_SAFE_JAM: "SSP_POLL_SAFE_JAM",
    SSP_POLL_UNSAFE_JAM: "SSP_POLL_UNSAFE_JAM",
    SSP_POLL_DISABLED: "SSP_POLL_DISABLED",
    SSP_POLL_FRAUD_ATTEMPT: "SSP_POLL_FRAUD_ATTEMPT",
    SSP_POLL_STACKER_FULL: "SSP_POLL_STACKER_FULL",
    SSP_POLL_NOTE_CLEARED_FROM_FRONT: "SSP_POLL_NOTE_CLEARED_FROM_FRONT",
    SSP_POLL_NOTE_CLEARED_TO_CASHBOX: "SSP_POLL_NOTE_CLEARED_TO_CASHBOX",
    SSP_POLL_CASHBOX_REMOVED: "SSP_POLL_CASHBOX_REMOVED",
    SSP_POLL_CASHBOX_REPLACED: "SSP_POLL_CASHBOX_REPLACED",
    SSP_POLL_BARCODE_TICKET_VALIDATED: "SSP_POLL_BARCODE_TICKET_VALIDATED",
    SSP_POLL_BARCODE_TICKET_ACK: "SSP_POLL_BARCODE_TICKET_ACK",
    SSP_POLL_NOTE_PATH_OPEN: "SSP_POLL_NOTE_PATH_OPEN",
    SSP_POLL_CHANNEL_DISABLE: "SSP_POLL_CHANNEL_DISABLE",
    SSP_POLL_INITIALISING: "SSP_POLL_INITIALISING",

}


import json

CFG = json.load(open('config.json', 'r', encoding='utf-8'))


class Casher():
    def __init__(self,com,ui):

        self.dll = windll.LoadLibrary("ITLSSPProc.dll")
        self.ui = ui
        self.value = 0
        self.timeout = CFG['TIMEOUT']
        self.isopen= -1
        self.openDevice(com)  # 传入的参数即串口序号
        self.currentTime = 0

    def __CheckGenericResponses(self, cmd):
        rd = cmd.ResponseData[0]
        if rd == SSP_RESPONSE_CMD_OK:
            return True
        else:
            # print(RESPONSE_NAMES[rd])
            return False


    def openDevice(self,comPort):
        # 打开并初始化设备

        # 打开串口
        commandStructure.PortNumber = comPort
        res = self.dll.OpenSSPComPortUSB(byref(commandStructure))
        print("OpenSSPComPortUSB", res)
        if res == 1:
            print('打开串口成功')
            self.ui.logUi.log('吃钞机正在启动')
            self.isRunning = True
        else:
            self.ui.logUi.log('吃钞机启动失败，请检查接线是否正确')
           # raise KeyError("接线错误或接触不良")
        self.isopen = res

        # 协商密钥
        keys = SSP_KEYS()
        commandStructure.EncryptionStatus = False
        commandStructure.CommandData[0] = SSP_CMD_SYNC
        commandStructure.CommandDataLength = 1
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("ssp_cmd_sync", res)

        res = self.dll.InitiateSSPHostKeys(byref(keys), byref(commandStructure))
        print("InitiateSSPHostKeys res", res)

        commandStructure.CommandData[0] = SSP_CMD_SET_GENERATOR
        commandStructure.CommandDataLength = 9
        for i in range(9):
            commandStructure.CommandData[i + 1] = keys.Generator >> (8 * i)
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_SET_GENERATOR", res)

        commandStructure.CommandData[0] = SSP_CMD_SET_MODULUS
        commandStructure.CommandDataLength = 9
        for i in range(9):
            commandStructure.CommandData[i + 1] = keys.Modulus >> (8 * i)
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_SET_MODULUS", res)

        commandStructure.CommandData[0] = SSP_CMD_KEY_EXCHANGE
        commandStructure.CommandDataLength = 9
        for i in range(9):
            commandStructure.CommandData[i + 1] = keys.HostInter >> (8 * i)
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_KEY_EXCHANGE", res)

        kk = 0
        keys.SlaveInterKey = 0
        for i in range(9):
            kk += (commandStructure.ResponseData[1 + i] << (8 * i))
        keys.SlaveInterKey = kk
        self.dll.CreateSSPHostEncryptionKey(byref(keys))

        commandStructure.Key.FixedKey = 0x0123456701234567
        commandStructure.Key.EncryptKey = keys.KeyHost
        commandStructure.EncryptionStatus = True

        # 设定协议版本
        commandStructure.CommandData[0] = SSP_CMD_HOST_PROTOCOL_VERSION
        commandStructure.CommandData[1] = 7
        commandStructure.CommandDataLength = 2
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_HOST_PROTOCOL_VERSION", res)

        # 设定禁止项
        commandStructure.CommandData[0] = SSP_CMD_SET_INHIBITS
        commandStructure.CommandData[1] = 0xFF
        commandStructure.CommandData[2] = 0xFF
        commandStructure.CommandDataLength = 3
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_SET_INHIBITS", res)

        # 初始化请求
        commandStructure.CommandData[0] = SSP_CMD_SETUP_REQUEST
        commandStructure.CommandDataLength = 1
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("SSP_CMD_SETUP_REQUEST", res)


    def stopDevice(self):
        # 关闭设备
        commandStructure.CommandData[0] = SSP_CMD_RESET
        commandStructure.CommandDataLength = 1
        info.CommandName = CMD_NAMES[SSP_CMD_RESET]
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        self.__CheckGenericResponses(commandStructure)
        print("reset:", res)
        self.dll.CloseSSPComPortUSB()


    def startToRecvCash(self):
        commandStructure.CommandData[0] = SSP_CMD_ENABLE
        commandStructure.CommandDataLength = 1
        info.CommandName = CMD_NAMES[SSP_CMD_ENABLE]
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("enable:", res)
        self.__CheckGenericResponses(commandStructure)


    def state(self):
        # 查询吃钞状态
        commandStructure.CommandData[0] = SSP_CMD_POLL
        commandStructure.CommandDataLength = 1
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"*****************************************SSP_CMD_POLL", res, "responseDataLen:", commandStructure.ResponseDataLength)
        resData = commandStructure.ResponseData[1:commandStructure.ResponseDataLength]
        if len(resData) != 1:  # 空闲状态，不打印了
            for r in range(len(resData)):
                x = resData[r]
                # print("POLL-%d/%d:"%(r,len(resData)),RESPONSE_NAMES[x] if x in RESPONSE_NAMES else hex(x))
                print("POLL-%d/%d:" % (r, len(resData)+1), RESPONSE_NAMES[x] if x in RESPONSE_NAMES else x)
                # if resData[r] ==SSP_POLL_CREDIT:
                #     self.value = money[resData[r+1]]
                #     print('value is %d'% self.value)
                # elif resData==SSP_POLL_STACKER_FULL:
                #     print('钱箱已满')
                #     self.ui.logUi.log('钱箱已满，请及时清空')
            if commandStructure.ResponseDataLength == 5 and commandStructure.ResponseData[4] == SSP_POLL_STACKED:
          #  if commandStructure.ResponseData[4] == SSP_POLL_STACKED or commandStructure.ResponseData[4] == SSP_POLL_STACKING :
                value = commandStructure.ResponseData[2]
                self.value=money[value]
                print('value is %d' % self.value)
            elif commandStructure.ResponseDataLength == 3 and commandStructure.ResponseData[1] == SSP_POLL_CREDIT:
                value = commandStructure.ResponseData[2]
                self.value = money[value]
                print('value is %d' % self.value)
            elif commandStructure.ResponseDataLength == 6 and commandStructure.ResponseData[5]==SSP_POLL_STACKER_FULL:
                print('钱箱已满')
                self.ui.logUi.log('钱箱已满，请及时清空')
            elif commandStructure.ResponseData[ commandStructure.ResponseDataLength-1] == SSP_POLL_DISABLED:
                self.startToRecvCash()
            elif commandStructure.ResponseData[1]== SSP_POLL_NOTE_READ:
                if self.timeout - self.currentTime <2 :
                    print('距离超时%f秒,加时5秒' % (self.timeout - self.currentTime))
                    self.timeout += 5


     #   time.sleep(1)





    def finishRecvCash(self):
        commandStructure.CommandData[0] = SSP_CMD_DISABLE
        commandStructure.CommandDataLength = 1
        info.CommandName = CMD_NAMES[SSP_CMD_DISABLE]
        res = self.dll.SSPSendCommand(byref(commandStructure), byref(info))
        print("disable:", res)
        self.__CheckGenericResponses(commandStructure)



    def getMoney(self,com,cost):
        '''支付（收钱）'''
        self.openDevice(com)  # 传入的参数即串口序号
        time.sleep(1)
        self.startToRecvCash()

        while self.isRunning:
            # for i in range(100):
            # time.sleep(1)
            self.state()
            if total == cost:
                break
            else:
                print('还差%d元' % (cost - total))

        self.finishRecvCash()
        self.stopDevice()
        time.sleep(1)

    def TestMoney(self,cost):
        '''支付（收钱）'''
        # time.sleep(1)
        self.startToRecvCash()
        status = 'false'

        while  self.currentTime<self.timeout:
          #  time.sleep(20)
            self.state()
            if self.value == 0:
                time.sleep(0.5)
                self.currentTime+=0.5
                if  self.currentTime >= self.timeout:
                    self.ui.logUi.log('等待超时')
            else:
                self.ui.logUi.log('结束吃钞')
                if self.value == cost:
                    status='true'
                else:
                    print('金额错误')
                    status ='false'
                if cost==100:
                    status='Err'
                break

        self.isRunning = False
        self.ui.emit(self.ui.CASHTEST, cost, status)
        self.finishRecvCash()
        self.dll.CloseSSPComPortUSB()


    def copyMC(self):
        self.startToRecvCash()

        while self.isRunning :
            time.sleep(0.05)
            self.state()
        self.finishRecvCash()
        self.dll.CloseSSPComPortUSB()


# if __name__ == '__main__':
#     casher = Casher(None)
#     casher.TestMoney(3,5)
