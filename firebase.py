import Adafruit_DHT
import time
import Rpi.GPIO as GPIO
from firebase import firebase
GPIO.setmode(GPIO.BCM)
firebase=firebase.FirebaseApplication("https://autobots-219104.firebaseio.com/")
result=firebase.post('/user','gayu')
print(result)
def dht11():
    sensor=Adafruit_DHT.DHT11
    gpio=17
    humidity,temperature=Adafruit_DHT.read_retry(sensor,gpio)
    while True:
        if humidity is not None and temperature is not None:
            return (temperature,humidity)
        else:
            return 0
        time.sleep(3)
var=dht11() 
sen_data=firebase.post('/user',var)
def moisture():
    channel = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    def callback(channel):
        if GPIO.input(channel):
            	return (1)
        else:
               return (0)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
while True:
	time.sleep(1)
water_data=moisture()
sen_data1=firebase.post('/user',water_data)
