import RPi.GPIO as GPIO

def blink_High(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	
def blink_Low(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)

if __name__ == "__main__":
		blink_High(4)
		
