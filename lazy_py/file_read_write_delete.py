#-*- coding:utf-8 -*-

import os
import time

def file_read_write_delete()
	print "Start file_read_write_delete test"
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
	time.sleep(60)
	os.system("")
	print "reboot end.\n\nfile_read_write_delete_ing"

def main()
	file_read_write_delete()

if __name__ == '__main__':
	main()