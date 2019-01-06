import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print("Message payload=", message.payload)
########################################

#broker_address="iot.eclipse.org"
broker_address="broker.hivemq.com"
subscribetopic = topic = "arachnovato/falcon/player/FPP/+"


print("creating new instance")
client = mqtt.Client("P100178") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic",subscribetopic)
client.subscribe(subscribetopic)
time.sleep(800) # wait
client.loop_stop() #stop the loop
