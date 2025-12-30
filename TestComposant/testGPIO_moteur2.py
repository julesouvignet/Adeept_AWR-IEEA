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

def motorStop(): # Stop motor rotation
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)

def setup(): # GPIO initialization, GPIO motor cannot be controlled without initialization
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    motorStop() # Avoid motor starting to rotate automatically after initialization
    try: # Try is used here to avoid errors due to repeated PWM settings
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass

def motor_A(direction, speed): # The function used to control the motor of port A
    if direction == 1:
        GPIO.output(Motor_A_Pin1, GPIO.HIGH)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)
    if direction == -1:
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.HIGH)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)

def motor_B(direction, speed): # The function used to control the motor of port B
    if direction == 1:
        GPIO.output(Motor_B_Pin1, GPIO.HIGH)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        pwm_B.start(100)
        pwm_B.ChangeDutyCycle(speed)
    if direction == -1:
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.HIGH)
        pwm_B.start(100)
        pwm_B.ChangeDutyCycle(speed)

try:
    print("\nsetup")
    setup()
    
    print("\nRun Moteur A + ")
    motor_A(1, 100)
    print("\nRun Moteur B + ")
    motor_B(1, 100)
    time.sleep(3)

    print("\nRun Moteur A - ")
    motor_A(-1, 100)
    print("\nRun Moteur B - ")
    motor_B(-1, 100)
    time.sleep(3)
    
    motorStop()
finally:
    GPIO.cleanup()
