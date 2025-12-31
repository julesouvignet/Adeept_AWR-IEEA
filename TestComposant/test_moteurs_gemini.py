import time
import Adafruit_PCA9685

# Initialisation du contrôleur PWM (adresse I2C par défaut 0x40)
#pwm = Adafruit_PCA9685.PCA9685()
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm.set_pwm_freq(60)

# Définition des canaux PWM pour les moteurs du robot Adeept AWR
# Canal 0 & 1 : Moteurs Gauches | Canal 2 & 3 : Moteurs Droits
MOTORS = {
    "GAUCHE_AVANT": 0,
    "GAUCHE_ARRIERE": 1,
    "DROIT_AVANT": 2,
    "DROIT_ARRIERE": 3
}

def moteur_on(canal):
    print(f"Test du canal {canal}...")
    # 4095 correspond à la vitesse maximale (cycle de service 100%)
    pwm.set_pwm(canal, 0, 4095)
    time.sleep(2)
    pwm.set_pwm(canal, 0, 0) # Arrêt

try:
    print("Début du test unitaire des moteurs")
    for nom, canal in MOTORS.items():
        moteur_on(canal)
        time.sleep(1)
    print("Test terminé.")

except Exception as e:
    print(f"Erreur lors du test : {e}")
