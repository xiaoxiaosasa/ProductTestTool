# -*- coding: UTF-8 -*-
# author:yuliang
import time
class Music:
    def __init__(self):
        self.isRunning = True

    def play(self,filename):
        import os
        try:
            while self.isRunning:
                os.system(filename)
                time.sleep(2*60)
        except Exception as e:
            print(e)
            raise KeyError('文件打开错误')



# import time
# import pygame
# # file=r'1.mp3'
# pygame.mixer.init()
# print("播放音乐")
# track = pygame.mixer.music.load('1.mp3')
#
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()
