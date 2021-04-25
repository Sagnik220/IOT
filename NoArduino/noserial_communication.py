from serial_class import NoArduinoComm
from time import sleep
import numpy as np
import pandas as pd

#ser = serial.Serial('/dev/tty.usbmodem14101', 9600)     # port, baud rate
ser=NoArduinoComm()
sensor_data = []    # list to store sensor data
count_arr = []  # count list

for i in range(0, 7):
    sensor_data.append(ser.randval_genarator(start=1,end=20))
    count_arr.append(i)
    sleep(1)

print(np.average(sensor_data))

values = {"Count": count_arr, "Sensor_data": sensor_data}
df_w = pd.DataFrame(values, columns=["Count", "Sensor_data"])
df_w.to_csv("sensor_data.csv", index=None, header=True)