import requests
import json

url = "https://api.thingspeak.com/channels/1368489/fields/1.json?api_key=1DBKVJNE8XY10ANB&results=2"

response = json.loads(requests.get(url).content)

print(float(response['feeds'][0]['field1']))