from machine import Pin, PWM
import time

led = machine.Pin(17,machine.Pin.OUT)  #LED

pwm  = machine.PWM(led)

pwm.freq(5000)  # Freq PWM = 5000Hz

while True:
    for i in range(0,65535,100):
        pwm.duty_u16(i)  # 0 = 0% 65535 = 100%
        time.sleep(0.005)
    for i in range(65535,0,-100):
        pwm.duty_u16(i)  # 0 = 0% 65535 = 100%
        time.sleep(0.005)