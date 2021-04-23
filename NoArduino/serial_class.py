#Importing the dependencies
import serial
from time import sleep
import numpy as np
import pandas as pd
import random

#Defining the Class ArduinoComm
class NoArduinoComm:
    sensor_data = []  # list to store sensor data
    count_arr = []  # count list

    def __init__(self):
        pass

    def randval_genarator(self,start,end):
        for i in range(start,end):
            n = random.randint(0,40)
            self.sensor_data.append(n)
            self.count_arr.append(i)
        return self.sensor_data,self.count_arr
        
    '''def connectWith(self, number, delay=1):
        ser = serial.Serial(self.serialPort, self.baudRate)
        for itr in range(0, number):
            self.sensor_data.append(float(ser.read(7).decode().strip()))
            self.count_arr.append(itr)
            print('.', end='')
            sleep(delay)
        print('\n')'''

    def calculateAverage(self):
        return round(np.average(self.sensor_data), 2)

    def writeCSV(self, fileName):
        values = {"Count": self.count_arr, "Sensor_data": self.sensor_data}
        df_w = pd.DataFrame(values, columns=["Count", "Sensor_data"])
        df_w.to_csv(fileName, index=None, header=True)