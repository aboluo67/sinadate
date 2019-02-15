# -*- coding: utf-8 -*-

import time
import pygame


# file=r'/Users/zoutao/Desktop/music/Dave Koz  I Believe.flac'
file=r'/Users/zoutao/Desktop/music/Klaus Badelt - He s A Pirate.flac'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(18.6)
pygame.mixer.music.stop()