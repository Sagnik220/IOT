from serial_class import NoArduinoComm
# We cant use it this way without Arduino as its using a Serial Port.
myObj = NoArduinoComm()
myObj.randval_genarator(start=1,end=20)
myObj.calculateAverage()
print("The avg. is: {avg:.2f}".format(avg=myObj.calculateAverage()))

myObj.writeCSV('results.csv')