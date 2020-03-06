import Adafruit_DHT
import time
import sys
import pandas as pd
from datetime import datetime

#Defining a dictionary to build the temp and humidity datas
data = {'Temperature (F)': [],'Humidity (%)':[], 'Date':[]}

#Converting the dictionary into a DataFrame
df = pd.DataFrame(data)

while True:
    current_date = datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    if humidity is not None and temperature is not None:
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)      
        #print('Temp: {0:0.1f} C    Humidity: {0:1.1f} %'.format(temperature, humidity))
        #print(temperature, humidity)
    
        temp_in_F = temperature * 1.8 + 32
        readings = pd.DataFrame({'Temperature (F)': [temp_in_F],'Humidity (%)': [humidity], 'Date':[current_date]})
        df = pd.concat([readings, df]).reset_index(drop=True)
        print("df")
        print(df)
        print()
    
    else:
        print('can not connect the sensor')
    
    
    time.sleep(300)
    df.to_csv('Temp_and_Hum1.csv')
            
    
    
     