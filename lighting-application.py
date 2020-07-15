import wiotp.sdk.application
from phue import Bridge

myConfig = wiotp.sdk.application.parseConfigFile("appconfig.yaml")
client = wiotp.sdk.application.ApplicationClient(config=myConfig, logHandlers=None)
client.connect()

b = Bridge('IP of your bridge')
b.connect()

def myEventCallback(event):
    data = event.data
    if data.get("statusA") == "dark" and data.get("statusB") == "dark":
        b.set_light(1,'on', True)
    if data.get("statusA") == "light" and data.get("statusB") == "light":
        b.set_light(1,'on', False)
    
while(1):
    client.deviceEventCallback = myEventCallback
    client.subscribeToDeviceEvents()
    

    
