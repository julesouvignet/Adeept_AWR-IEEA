import RPi.GPIO as GPIO
import time

# Utilisation du numéro de Pin GPIO 18
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuration du PWM à 50Hz (standard pour les servos)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    # Formule pour convertir l'angle en cycle opératoire (duty cycle)
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    print("Test du servo sur GPIO 18 (0, 90, 180 degrés)")
    while True:
        set_angle(0)
        time.sleep(1)
        set_angle(90)
        time.sleep(1)
        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Test arrêté.")
