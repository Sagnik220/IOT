import requests
from serial_class import NoArduinoComm

url = 'https://api.thingspeak.com/update?api_key=GMK3XQUBWS68VINW&field1=0'

myObj =NoArduinoComm()

i = 0
while i <= 3:
    myObj.randval_genarator(start=1,end=20)
    temp_data = myObj.calculateAverage()
    update = {'field1': temp_data}  # payload
    response = requests.get(url, data=update)
    print(response)
    i = + 1