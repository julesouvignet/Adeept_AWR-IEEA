import RPi.GPIO as GPIO
import time
Tr = 11 # Pin number of input terminal of ultrasonic module
Ec = 8 # Pin number of output terminal of ultrasonic module

GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)

def checkdist():
  GPIO.output(Tr, GPIO.HIGH) # Set the input end of the module to high level and emit an initial sound wavetime.sleep(0.000015)
  GPIO.output(Tr, GPIO.LOW)

  while not GPIO.input(Ec): # When the module no longer receives the initial sound wave
    pass
  
  t1 = time.time() # Note the time when the initial sound wave is emitted
  while GPIO.input(Ec): # When the module receives the return sound wave
    pass

  t2 = time.time() # Note the time when the return sound wave is captured
  
  return round((t2-t1)*340/2,2) # Calculate distance

for i in range(10):
  print(checkdist())
  time.sleep(1)
