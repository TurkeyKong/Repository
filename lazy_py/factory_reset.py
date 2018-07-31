#-*- coding:utf-8 -*-

import os
import time

def factory_reset()
	print "Start factory reset test"
	print "db root\n\n"
	os.popen("adb root")
	time.sleep(5)
	print "adb remount\n\n"
	os.popen("adb remount")
	time.sleep(1)
	print "adb push *** /system/vendor/app\n\n"
	os.popen("adb push *** /system/vendor/app")
	print "push successfully!!\n\n"
	os.system("adb reboot")
	print "reboot end.\n\nFactory reseting"

def main()
	factory_reset()

if __name__ == '__main__':
	main()
