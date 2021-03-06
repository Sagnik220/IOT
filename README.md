## IOT

### Setting Up Locally:
1. Creating the Virtual Environment
2. python -m venv env
3. Activating the Environment
4. env\Scripts\activate

### Dependencies:
```
- pip install paho-mqtt
- pip install numpy
- pip install pandas
- pip install sklearn
- pip install pyserial
- pip install requests

```

### What to use?
1. If you have Arduino go to Arduino Folder to execute the files,though you will need to generate a new API key for your thingspeak account
2. If you do not have the Arduino then go to NoArduino folder to test the files.

### Mqtt Publish/Subscribe:

The first concept is the publish and subscribe system. In a publish and subscribe system, a device can publish a message on a topic, or it can be subscribed to a particular topic to receive messages

1. For example Device 1 publishes on a topic.
2. Device 2 is subscribed to the same topic as device 1 is publishing in.
3. So, device 2 receives the message.

#### Workflow

<img src="Images/pubsubflow.jpg" height="200px">

**1. Mqtt-Publish/mqtt-publish.py**

<img src="Images/mqttscreenshot2.jpg" height="300px">

**2. Mqtt-Subscribe/mqtt-subscribe.py**

<img src="Images/mqttscreenshot1.jpg" height="300px">
<img src="Images/suboutput.jpg" height="250px">

### REST-GET:
We are using a REST API to connect the data from local system to the cloud platform,we are plotting the average value of sensor data we collected from local and plot it against time in the Thingspeak platform.

1. Code Execution
<img src="Images/rest.png">

2. Data Representation in Thingspeak
<img src="Images/thingspeak sensordata.png">

