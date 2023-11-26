#import pickle
from gpiozero import LED
from w1thermsensor import W1ThermSensor, Sensor

axt = LED(17)
axt.on()

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

Print(str(sensor_list))

while True:
    query = "http://XXXXXXX/HHHHHH/GET=YYYYYYYY"
    for sensor in W1ThermSensor.get_available_sensors():
        Print(sensor_list[sensor.id]["location"] + "reads" + str(sensor.gettemperature()))
        query += "&" + sensor_list[sensor.id]["thingspeak"] + "=" + str(sensor.gettemperature()))
    Print(query)
    #Print(curl query)
    sleep(60)
