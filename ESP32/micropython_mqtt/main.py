import network
from mqtt import MQTTClient 
import machine 
import time 
 
def sub_cb(topic, msg): 
   print("message recived {}".format(msg))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect("boba", "ilikeicecreammochi")

 
while not wlan.isconnected():  
    machine.idle() 
print("Connected to Wifi\n") 
 
client = MQTTClient("1234", "192.168.1.155",user="", password="", port=1883) 
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="esp/testtopic") 
while True:
    print("starting to listen on the topic")
    client.check_msg()

    #print("Sending ON") 
    #client.publish(topic="esp/testtopic", msg="ON")
    #time.sleep(1) 
    #print("Sending OFF") 
    #client.publish(topic="esp/testtopic", msg="OFF")
    time.sleep(1) 
