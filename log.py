from gpiozero import LED
from w1thermsensor import W1ThermSensor, Sensor


axt = LED(17)
axt.on()

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
