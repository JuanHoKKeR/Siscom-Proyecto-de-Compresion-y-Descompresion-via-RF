from machine import Pin, ADC, UART, Timer
import time

# Configuración del ADC y UART
adc = ADC(Pin(26))  # Asume que estás usando el GPIO 26 para el ADC
tx_pin = Pin(0, Pin.OUT)  # Ajusta este valor según tu configuración
uart = UART(0, baudrate=25000, tx=tx_pin)
led = Pin(25, Pin.OUT)


# Función para leer del ADC y comprimir los datos
def compresion():
    try:
        valor_adc = adc.read_u16()
        return valor_adc >> 8  # Comprime de 16 bits a 8 bits
    except Exception as e:
        print("Error al leer el ADC:", e)
        return 0

# Función para enviar datos
def enviar_numero(t):
    numero = compresion()
    uart.write(bytes([numero]))

# Configuración del Timer para enviar datos regularmente
tim = Timer()
tim.init(freq=50000, mode=Timer.PERIODIC, callback=enviar_numero)

# LED para indicar actividad
while True:
    led.toggle()
    time.sleep(0.5)