import machine
import _thread
from time import sleep

led_red = machine.Pin(0, machine.Pin.OUT)
led_green = machine.Pin(1, machine.Pin.OUT)

sLock = _thread.allocate_lock()

def CoreTask():
    while True:
        sLock.acquire()
        print("Enter second Thred")
        sleep(1)
        led_green.high()
        print("Green LED is turned ON")
        sleep(2)
        led_green.low()
        print("Green LED is turned OFF")
        sleep(1)
        print("Exit second Thread")
        sleep(1)
        sLock.release()
_thread.start_new_thread(CoreTask, ())

while True:
    sLock.acquire()
    print("Enter main Thread")
    led_red.toggle()
    sleep(0.15)
    print("Red LED toggling...")
    sleep(1)
    print("Exit main Thread")
    sleep(1)
    sLock.release()