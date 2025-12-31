import RPi.GPIO as GPIO
import time
 
# Configuration des broches
# Moteurs A et B (tes réglages)
Motor_A_EN, Motor_A_Pin1, Motor_A_Pin2 = 4, 14, 15
Motor_B_EN, Motor_B_Pin1, Motor_B_Pin2 = 17, 27, 18

# Initialisation
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def config_moteur(en, p1, p2):
    GPIO.setup(en, GPIO.OUT)
    GPIO.setup(p1, GPIO.OUT)
    GPIO.setup(p2, GPIO.OUT)

def action_moteur(en, p1, p2, nom):
    print(f"Activation : {nom}")
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(p1, GPIO.HIGH)
    GPIO.output(p2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(en, GPIO.LOW)
    print(f"Arrêt : {nom}")

# Configuration de tous les moteurs
moteurs = [
    (Motor_A_EN, Motor_A_Pin1, Motor_A_Pin2, "Moteur A (Avant Gauche)"),
    (Motor_B_EN, Motor_B_Pin1, Motor_B_Pin2, "Moteur B (Avant Droit)")
]

try:
    for en, p1, p2, nom in moteurs:
        config_moteur(en, p1, p2)
        action_moteur(en, p1, p2, nom)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print("Test terminé.")
