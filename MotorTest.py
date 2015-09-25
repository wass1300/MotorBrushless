import RPi.GPIO as GPIO
import time
import sys #récupérer arguments

# Commandes du moteur
# EN    IN1   IN2    RESULTAT
# ------------------------------
# PWM   H     L      tout droit
# PWM   L     H      sens inverse
# PWM   L     L      stop
# PWM   H     H      stop
# L     X     X      stop
# ------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_PWM, GPIO.OUT, initial = GPIO.LOW)
	
# Variables locales des données initiales du système
frequence_PWM = 200
duty_cycle = 50.0
pin_PWM = 18
pin_IN1 = 27
pin_IN2 = 22
pin_IN3 = 23
pin_IN4 = 24
p = GPIO.PWM(channel, frequence)
		
# Initialisation du programme de commande
def init():
	GPIO.setup(pin_IN1, GPIO.OUT)
	GPIO.setup(pin_IN2, GPIO.OUT)
	GPIO.setup(pin_IN3, GPIO.OUT)
	GPIO.setup(pin_IN4, GPIO.OUT)
	

# Tout droit
def go_ahead():
	p.start(duty_cycle)
	GPIO.output(pin_IN1, GPIO.HIGH)
	GPIO.output(pin_IN2, GPIO.LOW)
	GPIO.output(pin_IN3, GPIO.HIGH)
	GPIO.output(pin_IN4, GPIO.LOW)
	
# Tourner à Gauche
def turn_left():
	p.start(duty_cycle)
	GPIO.output(pin_IN1, GPIO.LOW)
	GPIO.output(pin_IN2, GPIO.HIGH)
	GPIO.output(pin_IN3, GPIO.HIGH)
	GPIO.output(pin_IN4, GPIO.LOW)
	
# Tourner à Droite
def turn_right():
	p.start(duty_cycle)
	GPIO.output(pin_IN1, GPIO.HIGH)
	GPIO.output(pin_IN2, GPIO.LOW)
	GPIO.output(pin_IN3, GPIO.LOW)
	GPIO.output(pin_IN4, GPIO.HIGH)

# Sens inverse
def go_reverse():
	p.start(duty_cycle)
	GPIO.output(pin_IN1, GPIO.LOW)
	GPIO.output(pin_IN2, GPIO.HIGH)
	GPIO.output(pin_IN3, GPIO.LOW)
	GPIO.output(pin_IN4, GPIO.HIGH)
	
# Stop
def stop():
	GPIO.output(pin_PWM, GPIO.LOW)
	#p.stop()
	
# Choix des commandes selon l'argument 
# 1 pour tout droit
# 2 pour autre sens 
# 3 pour tourner gauche
# 4 pour tourcher droite
def commande(arg):
	options = {
		'1'	: go_ahead,
		'2' : go_reverse,
		'3' : turn_left,
		'4' : turn_right
		}
	if arg in options:
        options[arg]()
    else:
        print 'Pas trouvé la fonction demandée!'
		
	
# Main programm
if __name__ == "__main__":
		commande(sys.argv[1])
		
