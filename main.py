from microbit import *
import machine

# Exemple d'utilisation d'une autre broche (P1)
servo_pin = machine.Pin(0)  # Changez le numéro de pin si nécessaire
pwm = machine.PWM(servo_pin)
pwm.freq(50)  # Fréquence pour les servos (50 Hz)

def set_angle(angle):
    """
    Définit l'angle du servomoteur.

    :param angle: Angle souhaité entre 0 et 180 degrés
    """
    duty = int(40 + (angle / 180) * 115)  # Ajuste les valeurs selon votre servo
    pwm.duty(duty)

# Tourner de 12 degrés
angle = 12
set_angle(angle)
sleep(1000)  # Attend que le servo se stabilise

# Arrête le PWM après usage
pwm.deinit()
