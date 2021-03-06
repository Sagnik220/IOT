import requests
from serial_class import ArduinoComm

url = 'https://api.thingspeak.com/update?api_key=5HPX7SD7SCNT10MP&'

myObj = ArduinoComm(serialPort='COM6', baudRate=9600)

i = 0
while i <= 3:
    myObj.connectWith(number=7, delay=1)
    temp_data = myObj.calculateAverage()
    update = {'field1': temp_data}  # payload
    response = requests.get(url, data=update)
    print(response)
    i = + 1