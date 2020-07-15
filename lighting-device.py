import RPi.GPIO as GPIO
import time
import wiotp.sdk.device

def eventPublishCallback():
	print('sent to cloud')


myConfig = wiotp.sdk.device.parseConfigFile('appconfig.yaml')
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()


GPIO.setmode(GPIO.BOARD)
pin_a = 7
pin_b = 40

def rc_time(pin):
	count = 0
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)

	GPIO.setup(pin,GPIO.IN)
	while GPIO.input(pin) == GPIO.LOW:
		if count>100000:
			break
		else:
			count+=1

	if count>10:
		if count>10000:
			count = 'dark'
	else:
		count = 'light'
	return count

while True:
	statusA = rc_time(pin_a)
	statusB = rc_time(pin_b)
	data = {"statusA":statusA, "statusB":statusB}
	client.publishEvent(eventId='event',msgFormat='json',data=data,qos=0,onPublish=eventPublishCallback)
	time.sleep(60)
