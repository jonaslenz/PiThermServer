#send requests to Web api
import requests
#read dict as real progress dict
import ast
#allow program to pause
from time import sleep
#power to the sensor by Gpio 17, as efficient hardware usage
from gpiozero import LED
#library for w1 sensors 
from w1thermsensor import W1ThermSensor, Sensor

axt = LED(17)
axt.on()
try:
    myFile = open('sample.txt', 'r')
    sensor_list = ast.literal_eval(myFile.read())
    myFile.close()
except:
    sensor_list = {}
    fieldid = 1
    for sensor in W1ThermSensor.get_available_sensors():
        sensor_list[sensor.id] = {"thingspeak":("field"+str(fieldid)), "location":"xx"}
        fieldid += 1
        if fieldid > 8:
            Print("Exeeding number of possible fields in free ThingSpeak.")
    myFile = open('sample.txt', 'w')
    myFile.write(str(sensor_list))
    myFile.close()
axt.off()
#print(str(sensor_list))

url = "http://XXXXXXX/HHHHHH/GET=YYYYYYYY"

while True:
    axt.on()
    payload = {}
    sleep(2)
    for sensor in W1ThermSensor.get_available_sensors():
        print(sensor_list[str(sensor.id)]["location"] + "reads" + str(sensor.get_temperature()))
        payload[sensor_list[str(sensor.id)]["thingspeak"]] = sensor.get_temperature()
    axt.off()

    #res = requests.post(url, data=payload)

    print(str(payload))
    #print(res)
    #res="last query not send."
    sleep(5)
