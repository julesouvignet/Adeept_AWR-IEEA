import RPi.GPIO as GPIO
import time

# Pin Definitions
Motor_A_EN = 4
Motor_B_EN = 17
Motor_A_Pin1 = 14
Motor_A_Pin2 = 15
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([Motor_A_EN, Motor_B_EN, Motor_A_Pin1, Motor_A_Pin2, Motor_B_Pin1, Motor_B_Pin2], GPIO.OUT)

# PWM for speed control
pwm_a = GPIO.PWM(Motor_A_EN, 1000)  # 1000Hz frequency
pwm_b = GPIO.PWM(Motor_B_EN, 1000)
pwm_a.start(0)  # Start with 0% duty cycle
pwm_b.start(0)

def forward(speed=100):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.HIGH)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)

def backward(speed=100):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)

def left(speed=100):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    GPIO.output(Motor_B_Pin1, GPIO.HIGH)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)

def right(speed=100):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)

def stop():
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

# Example usage
try:
    print("\nForward")
    forward(80)
    time.sleep(2)
    print("\nLeft")
    left(80)
    time.sleep(1)
    print("\nStop")
    stop()
except KeyboardInterrupt:
    print("\nArrêt demandé par l'utilisateur")
except Exception as e:
    print(f"\nUne erreur est survenue : {e}")
finally:
    # Nettoyage des GPIOs dans tous les cas
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
    print("Nettoyage des GPIOs terminé. Au revoir !")
