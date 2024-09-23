from machine import Pin, UART, PWM, Timer
import time

# Configuración del UART y PWM
rx_pin = Pin(1, Pin.IN)  # Ajusta este valor según tu configuración
uart = UART(0, baudrate=25000, rx=rx_pin)
led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))
pwm.freq(20000)

# Función para descomprimir y enviar a PWM
def recibir_y_procesar(t):
    if uart.any():
        dato = uart.read(1)
        if dato:
            numero_recibido = int.from_bytes(dato, 'big')
            valor_pwm = numero_recibido << 8
            pwm.duty_u16(valor_pwm)

# Configuración del Timer para leer datos regularmente
tim = Timer()
tim.init(freq=50000, mode=Timer.PERIODIC, callback=recibir_y_procesar)

# LED para indicar actividad
while True:
    led.toggle()
    time.sleep(0.5)