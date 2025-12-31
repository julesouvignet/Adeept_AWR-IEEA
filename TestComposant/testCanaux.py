import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def test_canal(canal):
    print(f"Test du Canal {canal}...")
    pwm.set_pwm(canal, 0, 400) # Signal de test
    time.sleep(2)
    pwm.set_pwm(canal, 0, 0)   # Arrêt
    time.sleep(1)

try:
    # On teste les 8 premiers canaux pour identifier les branchements
    for i in range(8):
        test_canal(i)

except KeyboardInterrupt:
    for i in range(16): pwm.set_pwm(i, 0, 0)
