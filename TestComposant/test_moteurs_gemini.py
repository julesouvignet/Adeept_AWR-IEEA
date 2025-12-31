import RPi.GPIO as GPIO
import time
 
# Configuration des broches
# Moteurs A et B (tes réglages)
Motor_A_EN, Motor_A_Pin1, Motor_A_Pin2 = 4, 14, 15
Motor_B_EN, Motor_B_Pin1, Motor_B_Pin2 = 17, 27, 18

# Moteurs C et D (broches standards Adeept)
Motor_C_EN, Motor_C_Pin1, Motor_C_Pin2 = 1, 7, 8
Motor_D_EN, Motor_D_Pin1, Motor_D_Pin2 = 16, 12, 16 # Attention: à vérifier selon ton câblage réel

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
    (Motor_B_EN, Motor_B_Pin1, Motor_B_Pin2, "Moteur B (Avant Droit)"),
    (Motor_C_EN, Motor_C_Pin1, Motor_C_Pin2, "Moteur C (Arrière Gauche)"),
    (Motor_D_EN, Motor_D_Pin1, Motor_D_Pin2, "Moteur D (Arrière Droit)")
]

try:
    for en, p1, p2, nom in moteurs:
        config_moteur(en, p1, p2)
        action_moteur(en, p1, p2, nom)
        time.sleep(0.5)

finally:
    GPIO.cleanup()
    print("Test terminé.")
