# -*- coding:utf-8 -*-

import os
import sys

vedio = '123 123'
firstvedio = '123 123'

next = '123 123'
previous = '123 132'
cmd = 'adb shell input tap'

print("Open vedio software")
os.system(cmd + vedio)
os.sleep(500)
print("Click the first vedio")
os.system(cmd + firstvedio)
os.sleep(300)

i, n = 1, 0
print("==============Start the real test=============")
while n < 2000:
    print('The %i times click: next' % i)
    os.system(cmd + next)
    os.sleep(300)
    print('The %i times click: next' % (i + 1))
    os.system(cmd + next)
    os.sleep(300)
    print('The %i times click: previous' % (i + 2))
    os.system(cmd + previous)
    os.sleep(300)
    print('The %i times click: previous' % (i + 3))
    os.system(cmd + previous)
    os.sleep(300)
    i += 4
