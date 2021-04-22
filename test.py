# This is test file using user define functions to import user defined class ArduinoComm and test its functions.

from serial_class import ArduinoComm
# We cant use it this way without Arduino as its using a Serial Port.
myObj = ArduinoComm(serialPort='', baudRate=115200)
myObj.connectWith(number=7, delay=2)

print("The avg. is: {avg:.2f}".format(avg=myObj.calculateAverage()))

myObj.writeCSV('results.csv')