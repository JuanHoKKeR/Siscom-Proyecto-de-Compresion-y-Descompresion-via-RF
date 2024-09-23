from machine import Pin, ADC, UART, Timer
import time

# Configuración del ADC y UART
adc = ADC(Pin(26))  # Asume que estás usando el GPIO 26 para el ADC
tx_pin = Pin(0, Pin.OUT)  # Ajusta este valor según tu configuración
uart = UART(0, baudrate=25000, tx=tx_pin)
led = Pin(25, Pin.OUT)


def alternative_bit_length(n):
    bits = 0
    while n:
        bits += 1
        n >>= 1
    return bits

# Función para comprimir los datos
def compresion(numero):
    try:
        msb = alternative_bit_length(numero)
        next_four_bits = (numero >> max(0, msb - 5)) & 0b1111 if msb > 1 else 0
        msb_minus_4 = max(0, msb - 4)
        comprimed8bits = (msb_minus_4 << 4) | next_four_bits
        return comprimed8bits
    except Exception as e:
        print("Error en compresión:", e)
        return 0

# Función para leer del ADC y enviar los datos comprimidos
def enviar_numero(t):
    valor_adc = adc.read_u16()
    numero_comprimido = compresion(valor_adc >> 8)
    uart.write(bytes([numero_comprimido]))

# Configuración del Timer para enviar datos regularmente
tim = Timer()
tim.init(freq=50000, mode=Timer.PERIODIC, callback=enviar_numero)

# LED para indicar actividad
while True:
    led.toggle()
    time.sleep(0.5)
