#import pickle
import requests
from gpiozero import LED
from w1thermsensor import W1ThermSensor, Sensor

axt = LED(17)

try:
    #sensor_list = pickle.load(sensordump)
    myFile = open('sample.txt', 'r')
    sensor_list = myFile.read()
    myFile.close()
except:
    sensor_list = {}
    fieldid = 1
    for sensor in W1ThermSensor.get_available_sensors():
        sensor_list[sensor.id] = {thingspeak:"field"+str(fieldid), location:"xx"}
        fieldid += 1
        if fieldwork > 8:
            Print("Exeeding number of possible fields in free ThingSpeak.")
    #pickle.dump(sensor_list,sensordump)
    myFile = open('sample.txt', 'w')
    myFile.write(str(sensor_list))
    myFile.close()

print(str(sensor_list))

url = "http://XXXXXXX/HHHHHH/GET=YYYYYYYY"
i=0
while i<10:
    axt.on()
    payload = {}
    sleep(2)
    for sensor in W1ThermSensor.get_available_sensors():
        print(sensor_list[sensor.id]["location"] + "reads" + str(sensor.gettemperature()))
        payload[sensor_list[sensor.id]["thingspeak"]] = sensor.gettemperature()
    axt.off()

    #res = requests.post(url, data=payload)

    print(str(payload))
    #print(res)
    #res="last query not send."
    sleep(60)
    i+=1
