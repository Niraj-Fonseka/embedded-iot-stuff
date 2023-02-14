
import time
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

wifi_name = "boba"
wifi_password = "ilikeicecreammochi"

print("Connecting to wifi")
wifi.radio.connect(wifi_name, wifi_password)
print("Connected to wifi")

### Feeds ###



def InitializeMQTT(connected_callback,on_disconnect_callback,on_message_callback):
    # Create a socket pool
    pool = socketpool.SocketPool(wifi.radio)

    # Set up a MiniMQTT Client
    mqtt_client = MQTT.MQTT(
        broker='192.168.1.152',
        port=1883,
        socket_pool=pool,
        #ssl_context=ssl.create_default_context(),
    )

    # Setup the callback methods abovea
    mqtt_client.on_connect = connected_callback
    mqtt_client.on_disconnect = on_disconnect_callback
    mqtt_client.on_message = on_message_callback

    # Connect the client to the MQTT broker.
    print("Connecting to Adafruit IO...")
    mqtt_client.connect()

    return mqtt_client
