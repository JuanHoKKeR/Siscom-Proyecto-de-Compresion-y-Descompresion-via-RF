from machine import Pin, Timer
import utime

# Configura el pin de transmisión
transmit_pin = Pin(15, Pin.OUT)  # Asumiendo que usas el GPIO 15
led = Pin(25, Pin.OUT)

def send_byte(data):
    led.value(0)
    for i in range(8):
        bit = (data >> i) & 1
        transmit_pin.value(bit)
        utime.sleep_ms(1)  # Espera 1 ms entre cada bit
    led.value(1)

# Envía un byte de prueba
while True:
    byte_to_send = 0xAB  # Cambia esto por el byte que desees enviar
    send_byte(byte_to_send)