import Adafruit_DHT
import time
import sys

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    if humidity is not None and temperature is not None:
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print('Temp: {0:0.1f} C    Humidity: {1:0.1f} %'.format(temperature, humidity))
    else:
        print('can not connect the sensor')
    time.sleep(10)
            
    
    
     