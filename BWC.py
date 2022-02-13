#!/usr/bin/env python 

from datetime import datetime
from time import strftime
import datetime, commands, re
import time, os.path
import os

image_frequency=0
logfile_path = '/media/pi/TIMELAPSER/log.txt'
image_target = '/var/www/html/image.jpg'
webpage_path = '/var/www/html/index.html'
logfile_path = '/var/www/html/log.txt'
current_timestamp = ''
image_cntr=1

time.sleep(30)

while True: 
	os.system("libcamera-jpeg -o " + image_target + " -n --width 800 --height 600 --rotation 180")
	image_cntr = image_cntr + 1
	with open(webpage_path,"w") as webpage:
				#logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Started!\n")
				webpage.write("<!DOCTYPE html>\n<html>\n   <head>\n <title>PieCam</title>\n\n <b>"+ (strftime("%Y-%m-%d %H:%M:%S")) +"</b><br><br> \n   </head>\n   <body>\n<img src=""image.jpg"">\n <br>\n      </body>\n</html>\n")
	time.sleep(1)
