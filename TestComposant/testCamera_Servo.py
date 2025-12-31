import Adafruit_PCA9685
import time

# Initialisation du contrôleur avec l'adresse I2C standard (0x40)
try:
    pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
    pwm.set_pwm_freq(50) # Fréquence standard de 50Hz pour les servos
    print("Contrôleur PCA9685 détecté. Début du test...")
    
    while True:
        print("Position 1 (300)")
        pwm.set_pwm(3, 0, 300) # Canal 3 (souvent utilisé pour la direction ou la caméra)
        time.sleep(1)
        
        print("Position 2 (400)")
        pwm.set_pwm(3, 0, 400)
        time.sleep(1)

except Exception as e:
    print(f"Erreur de communication I2C : {e}")
    print("Vérifiez que l'I2C est activé dans raspi-config et que le robot est alimenté.")
