import threading
import time
import serial
import rospy
from std_msgs.msg import *

try :
    nanoSerial = serial.Serial("/dev/ttyUSB0", 9600) 
except :
    print("please connect usb wire")

pm10_int=0
pm25_int=0
pm100_int=0
temp_int=0
hum_int=0

def arduino_driver():
    c=nanoSerial.read(6)
    while c !='$GNGGA':
        c=nanoSerial.read(6)
    print(c)
    gpsstr=nanoSerial.read(32)
    gpsstr=gpsstr.split(',') 
    print(gpsstr[2])
    fake=',055148,2407.8945,N,12041.7649,E,1,00,1.0,155.2,M,16.6,M,X.X,xxxx,*47'
    fake=fake.split(',')
    for i in range(5):
        print(fake[i])
    while c!='GNGGA':
        gpsstr=nanoSerial.read(32)
        # print(gpsstr)
        gpsstr.split(',') 
    # print(gpsstr[0])
    # if c=='G':
    #     c=nanoSerial.read(32)
    #     print(c)
    #     if c[31]=='E':
    #         gps_time=c[0:10]
    #         Lat=c[10:19]
    #         uLat=c[19:20]
    #         Lon=c[20:30]
    #         uLon=c[30:31]
                    # gps_sensor.publish(gps_time)
                    # gps_sensor.publish(Lat)
                    # gps_sensor.publish(uLat)
                    # gps_sensor.publish(Lon)
                    # gps_sensor.publish(uLon)
                    
        
# def talker():
    
    
    
   
    
#     rate = rospy.Rate(1) # 10hz
#     while not rospy.is_shutdown():
#         co2_sensor.publish(co2_int)
#         rate.sleep()

if __name__ == '__main__':
    arduino_driver()