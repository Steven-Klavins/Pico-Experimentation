from machine import Pin
from time import sleep

ledG = Pin(20, machine.Pin.OUT)
ledY = Pin(19, machine.Pin.OUT)
ledR = Pin(17, machine.Pin.OUT)

while True:
   
   
    ledR.value(1)
    sleep(0.5)
    ledR.value(0)
    ledY.value(1)
    sleep(0.5)
    ledY.value(0)
    ledG.value(1)
    sleep(0.5)
    ledG.value(0)
    
   
   
    
   
