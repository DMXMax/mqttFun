import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="iot.eclipse.org"
broker_address="broker.hivemq.com"
topic = "arachnovato/falcon/player/FPP/playlist/name/set"
playlist = "Production"
print("creating new instance")
client = mqtt.Client("P100177") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic",topic)
client.subscribe(topic)
print("Publishing message to topic",topic)
client.publish(topic, playlist)
time.sleep(8) # wait
client.loop_stop() #stop the loop
