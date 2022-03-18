#!/usr/bin/env python 

from datetime import datetime
from time import strftime
from shutil import copyfile
import datetime, commands, re
import time, os.path
import os

#========================= Constants definitions
image_frequency=0
logfile_path = '/home/pi/dev/BWC/BWC_log.txt'
image_target = '/var/www/html/image.jpg'
image_target_arch_folder = '/home/pi/dev/BWC/IMG'
image_target_arch_path = ''
webpage_path = '/var/www/html/index.html'
logfile_path = '/var/www/html/log.txt'
current_timestamp = ''
image_cntr=1

#========================= function definitions 
def log_to_file(func_logfile_path,func_content):
	"""This function logs the content string into a logfile in 
	Timestam,content string,<CR>
	format."""
	with open(func_logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+","+func_content+"\n")

#========================= Program entry point

log_to_file(logfile_path,"Application started")

#time.sleep(30)

while True: 
	os.system("libcamera-jpeg -o " + image_target + " -n --width 800 --height 600")
	image_target_arch_path = image_target_arch_folder + "/" + '{0:09}'.format(image_cntr)+".jpg"
	copyfile(image_target,image_target_arch_path)
	image_cntr = image_cntr + 1
	with open(webpage_path,"w") as webpage:
				#logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Started!\n")
				webpage.write("<!DOCTYPE html>\n<html>\n   <head>\n <title>PieCam</title>\n\n <b>"+ (strftime("%Y-%m-%d %H:%M:%S")) +"</b><br><br> \n   </head>\n   <body>\n<img src=""image.jpg"">\n <br>\n      </body>\n</html>\n")
	time.sleep(1)
