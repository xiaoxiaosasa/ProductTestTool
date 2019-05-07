# -*- coding: UTF-8 -*-
# author:yuliang  2019.03.15


import pyttsx3
import time

# class Speaker:
#     def __init__(self, rate=150,volume=1):
#         '''
#         初始化发音
#         :param rate:语速 默认200  Integer speech rate in words per minute
#         :param volume:音量 默认1  Floating point volume of speech in the range [0.0, 1.0]
#         :param num: 车牌号（str）
#         '''
#         self.engine = pyttsx3.init()
#         self.engine.setProperty('rate', rate)
#         self.engine.setProperty('volume', volume)
#
#     @classmethod
#     def speak(cls,txt):
#         cls.engine = pyttsx3.init()
#         # print(cls.engine.isBusy())
#         cls.engine.say(txt)
#         cls.engine.runAndWait()
#
#     def __del__(self):
#         self.engine.stop()
#         print('回收')
#
# if __name__ == '__main__':
#
#     Speaker.speak('车主您好，欢迎光临停车场')
#     Speaker.speak('车主您好，谢谢惠顾,您本次消费%.2f元'%10.8)


from threading import Condition, Thread
from _thread import start_new_thread

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak('')


class Speaker(Thread):

    def __init__(self, ui,rate=150, volume=1):
        self.ui=ui
        self.msgs = []
        self.cond = Condition()
        Thread.__init__(self)
        self.rate = rate
        self.volume = volume

    def speak(self, msg):
        self.cond.acquire()
        self.msgs.append(msg)
        self.cond.notify()
        self.cond.release()

    def run(self):

        # engine.setProperty('rate', self.rate)
        # engine.setProperty('volume', self.volume)
        while True:
            self.cond.acquire()
            if len(self.msgs) == 0:
                self.cond.wait()
                self.cond.release()
                # continue
            else:
                msg = self.msgs.pop(0)

                self.cond.release()
                self.__speak(msg)

    def __speak(self,msg):
        # engine.say(msg)
        # engine.runAndWait()
        # speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(msg)
        print(msg)



    def test(self,msg):
        self.speak(msg)
        # self.start()
        self.ui.emit(self.ui.VOICESTATUS)


if __name__ == '__main__':
    s = Speaker()
    s1 = Speaker()
    s.start()
    s1.start()
    s.speak('社会主义好')
    s1.speak('共产党万岁')
    s.speak('人民民主专政万岁')
    s1.speak("说完了")
    print("说完了1")









# 发音
# engine = pyttsx.init()
# engine.say(u'008号车主您好，欢迎光临')
# cost = input()
# engine.say(u'008号车出场，谢谢惠顾，您本次消费为%.2f元'%cost)
# engine.runAndWait()


# 事件监听
# import pyttsx
# def onStart(name):
#    print 'starting', name
# def onWord(name, location, length):
#    print 'word', name, location, length
# def onEnd(name, completed):
#    print 'finishing', name, completed
# engine = pyttsx.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say(u'你好，The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


# 打断发言
# import pyttsx
# def onWord(name, location, length):
#    print 'word', name, location, length
#    if location > 10:
#       engine.stop()
# engine = pyttsx.init()
# engine.connect('started-word', onWord)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# 改变音调
# engine = pyttsx.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say(u'你好 The quick brown fox jumped over the lazy dog.')  # 第二个发音人不识别中文
# engine.runAndWait()


# 改变语速

# engine = pyttsx.init()
# rate = engine.getProperty('rate')
# print rate
# engine.setProperty('rate', rate+100)
# engine.say(u'车主你好，欢迎光临，The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# 改变音量
# engine = pyttsx.init()
# volume = engine.getProperty('volume')
# print volume
# engine.setProperty('volume', volume+10)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# 事件驱动
# engine = pyttsx.init()
# def onStart(name):
#    print 'starting', name
# def onWord(name, location, length):
#    print 'word', name, location, length
# def onEnd(name, completed):
#    print 'finishing', name, completed
#    if name == 'fox':
#       engine.say('What a lazy dog!蓝狗', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
# engine = pyttsx.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()
