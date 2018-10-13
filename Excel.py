import os
import time 
from time import sleep
from datetime import datetime

file = open("/home/pi/data_log.csv", "a")
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
        file.write("Sensor1\n")
while True:
        i=i+1
        now = datetime.now()
        file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n")
        file.flush()
        
