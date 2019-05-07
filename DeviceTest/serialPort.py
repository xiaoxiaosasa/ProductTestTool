#coding=utf-8
#author:yuliang

import serial
import _thread
import time
#form _thread import start_new_thread

class Port:
    def __init__(self,port,ui):
        self.ui = ui
        self.info=None
        self.port = port
        try:
            self.serial = serial.Serial(self.port, baudrate=9600, timeout=1,
                                        parity=serial.PARITY_NONE)
           
        except Exception as e:
            print(e)

    def send(self,msg):
        if self.serial:
            print('send')
            self.serial.write(msg)

    def recv_rst(self):
        '''接收数据'''
        t=0
        while t<10:
            time.sleep(0.2)
            try:
                if self.serial and self.serial.in_waiting:
                    # info = self.serial.read(self.serial.in_waiting).decode('utf-8') 如果是中文,解码
                    self.info = self.serial.read(self.serial.in_waiting)
                    print(self.info)
                    self.serial.write(self.info)
                    break
            except Exception as e:
                print('send:', e)
            else:
                print('no data')
                t += 0.2
                if t==10:
                    self.ui.logUI.log('串口测试超时')
                    print('timeout')
        time.sleep(2)        
        self.serial.close()
        print('end')


class Connect():
    def __init__(self,com1,com2,ui):
        self.port1 = Port(com1,ui)
        self.port2 = Port(com2,ui)
        self.ui =ui

    def start(self):
        _thread.start_new_thread(self.port1.recv_rst,())
        _thread.start_new_thread(self.port2.recv_rst,())

        time.sleep(1)
        self.port1.send(b'hello')
        time.sleep(1)
        if self.port1.info and self.port2.info and self.port1.info == self.port2.info:
            print("com%s-com%s connected"%(self.port1.port,self.port2.port))
            self.ui.emit(self.ui.PORTCONNECT,'true')
        else:
            print("com%s-com%s disconnected" % (self.port1.port, self.port2.port))
            self.ui.emit(self.ui.PORTCONNECT,'false')


if __name__=='__main__':
    # s1 = Port('com1')
    # s2 = Port('com2')
    #
    # _thread.start_new_thread(s2.recv_rst,())
    # _thread.start_new_thread(s1.recv_rst,())
    # time.sleep(1)
    # s1.send(b'hello')
    # time.sleep(1)
    # if s1.info and s2.info and s1.info==s2.info:
    #     print('ok')
    
    con = Connect("com1","com2")
    con.start()
    
    
    
    
                
