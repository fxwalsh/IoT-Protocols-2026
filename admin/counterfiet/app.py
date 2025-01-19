from time import sleep

from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5000)

led = GroveLed(0)

while True:
    print('Turning LED off')
    led.off()
    sleep(2)
    print('Turning LED on')
    led.on()
    sleep(2)