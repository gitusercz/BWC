#!/usr/bin/env python 

from datetime import datetime
from time import strftime
from shutil import copyfile
import datetime, re
import time, os.path
import os

#========================= Constants definitions
config_file = '/home/pi/dev/BWC_pyth3/config.ini'
current_timestamp = ''
image_target_collection_path = ''
image_cntr=1

#========================= Constants load from config
from configobj import ConfigObj
config = ConfigObj(config_file)

logfile_path = config['Paths']['logfile']
image_target_for_webpage = config['Paths']['image_target_for_webpage']
image_target_collection_folder = config['Paths']['image_target_collection_folder']
webpage_path = config['Paths']['webpage_path']

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
	os.system("libcamera-jpeg -o " + image_target_for_webpage + " -n --width 800 --height 600")
	image_target_collection_path = image_target_collection_folder + "/" + '{0:09}'.format(image_cntr)+".jpg"
	copyfile(image_target_for_webpage,image_target_collection_path)
	image_cntr = image_cntr + 1
	with open(webpage_path,"w") as webpage:
				#logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Started!\n")
				webpage.write("<!DOCTYPE html>\n<html>\n   <head>\n <title>PieCam</title>\n\n <b>"+ (strftime("%Y-%m-%d %H:%M:%S")) +"</b><br><br> \n   </head>\n   <body>\n<img src=""image.jpg"">\n <br>\n      </body>\n</html>\n")
	time.sleep(1)
