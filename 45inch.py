import board
import neopixel
import math
import time
import digitalio
import analogio
import pulseio
from adafruit_motor import servo

def servoTop_duty_cycle(pulse_ms, frequency=300):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def servoBottom_duty_cycle(pulse_ms, frequency=300):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

servoTop = pulseio.PWMOut(board.D6, frequency=300)
servoBottom = pulseio.PWMOut(board.D7, frequency=300)
# pwm = pulseio.PWMOut(board.D5, frequency=50)
# my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

i = .95
b = 1.2
servoBottom.duty_cycle = servoBottom_duty_cycle(b)
time.sleep(.1)
servoTop.duty_cycle = servoTop_duty_cycle(i)

time.sleep(4)



while True:
    b = b + .02
    servoBottom.duty_cycle = servoBottom_duty_cycle(b)
    time.sleep(.01)
    if b > 1.4:
        i = i + .05
        b = b + .01
        servoTop.duty_cycle = servoTop_duty_cycle(i)
        servoBottom.duty_cycle = servoBottom_duty_cycle(b)
        time.sleep(.01)
        if i > 1.4:
            while True:
                print(b)
                time.sleep(2)

    # servoTop.duty_cycle = servoTop_duty_cycle(1.7)
#     time.sleep(2.0)
#     servo.duty_cycle = servo_duty_cycle(2.0)
#     time.sleep(1.0)















# for i in range (90, 120, 5):
#     time.sleep(0.5)
#     print(i)
#     my_servo.angle = i
# for i in range (140, 90, 5):
#     time.sleep(0.5)
#     print(i)
#     my_servo.angle = i


    #my_servo.angle = angle
# time.sleep(1)
