import ssd1306
import machine
import time
import uos
import machine
import network
from simple import MQTTClient

mqtt_server = '192.168.1.152'
client_id = 'test_assist'
topic_pub = b'lan_desk_assistant_pub'
topic_msg = b'lan_desk_assistant_connected'
topic_sub = b'lan_desk_assistant_sub'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("WIFI-NAME","WIFI-PWD")

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")
print("128x64 SSD1306 I2C OLED on Raspberry Pi Pico")

WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)
print("Available i2c devices: "+ str(i2c.scan()))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

owner_auto = False
owner_ok = False
owner_dnd = False
owner_call = False


reciever_ok = False
reciever_dnd = False
reciever_call = False

def print_state():
    print("reciver auto : " , reciever_auto)
    print("reciver ok : " , reciever_ok)
    print("reciver dnd : " , reciever_dnd)
    print("reciver call : " , reciever_call)
    print()


def sub_cb(topic, msg):
    global reciever_ok 
    global reciever_dnd 
    global reciever_call
    
    global owner_auto 
    global owner_ok 
    global owner_dnd 
    global owner_call
    print("New message on topic {}".format(topic.decode('utf-8')))
    msg = msg.decode('utf-8')
    print(msg)


    if msg == "ok_on":
        reciever_ok = True
    elif msg == "ok_off":
        reciever_ok = False
    elif msg == "dnd_on":
        print("dnd hitttt : ",reciever_dnd)
        reciever_dnd = True
        print(reciever_dnd)
    elif msg == "dnd_off":
        reciever_dnd = False
    elif msg == "call_on":
        reciever_call = True
    elif msg == "call_off":
        reciever_call = False
    
    print_state()

def wifi_setup():
    retry = 0
    while wlan.isconnected() == False:
        oled.text("WiFi Error", 20, 5)
        oled.text("Retries: {}".format(retry), 20, 25)
        oled.show()
        retry = retry + 1
        time.sleep(2)
        oled.fill(0)

    oled.text("WiFi Connected !", 0, 5)
    oled.show()
    time.sleep(1)

def mqtt_setup():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    
    while True:
        try:
            client.connect()
            print('client connected !')
            oled.text("MQTT Connected !", 0, 35)
            oled.show()
            time.sleep(1)
            client.publish(topic_pub, topic_msg)
            return client
        except OSError as e:
            print('Failed to connect to the MQTT Broker. Reconnecting...')
            oled.text("MQTT Error", 20, 45)
            oled.show()
            continue
        time.sleep(1)
        
    
def setup():
    print("in setup")
    wifi_setup()
    mqtt_client = mqtt_setup()
    
    print(mqtt_client)
    time.sleep(5)
    oled.fill(0)

    mqtt_client.publish(topic_pub, topic_msg)

    oled.text("AP", 10, 5)
    oled.text("Dnd", 40, 5)
    oled.text("Call", 72, 5)
    oled.text("Ok", 111, 5)

    oled.vline(35,0,64,1)
    oled.vline(68,0,64,1)
    oled.vline(106,0,64,1)

    oled.hline(35, 34, 128, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
    oled.hline(35, 45, 128, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
    oled.fill_rect(36, 35, 118, 10, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1
    oled.text("Niraj", 42, 36)


    return mqtt_client



def user_panel():

   global owner_auto 
   global owner_ok 
   global owner_dnd 
   global owner_call
   
   if owner_auto:
       oled.text("ON", 10, 25)
   else:
       oled.text("OFF", 8, 25)

   if owner_ok:
       oled.fill_rect(47, 19, 8, 7, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
   else:
       oled.fill_rect(47, 19, 8, 7, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1

   if owner_dnd:
       oled.fill_rect(82, 19, 8, 7, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
   else:
       oled.fill_rect(82, 19, 8, 7, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1
       
   if owner_call:
       oled.fill_rect(11, 19, 8, 7, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1  
   else:
       oled.fill_rect(114, 19, 8, 7, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1
       

def reciever_panel():
    
   global reciever_ok 
   global reciever_dnd 
   global reciever_call
   
   if reciever_ok:
       oled.fill_rect(47, 54, 8, 7, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
   else:
       oled.fill_rect(47, 54, 8, 7, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1
       
   if reciever_dnd:
       oled.fill_rect(82, 54, 8, 7, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
   else:
       oled.fill_rect(82, 54, 8, 7, 0)        # draw a rectangle outline 10,10 to 117,53, colour=1
       
   if reciever_call:
       oled.fill_rect(114, 54, 8, 7, 1)        # draw a rectangle outline 10,10 to 1
   else:
       oled.fill_rect(114, 54, 8, 7, 0)        # draw a rectangle outline 10,10 to 1
       



def main():
    client = setup()
    client.set_callback(sub_cb)

    oled.show()
    
    while True:
        client.subscribe(topic_sub)
        user_panel()
        reciever_panel()
        oled.show()
        
main()
