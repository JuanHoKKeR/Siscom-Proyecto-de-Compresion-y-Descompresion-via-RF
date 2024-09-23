from machine import Pin, ADC, Timer

# Configurar el pin de entrada analógica para el potenciómetro
adc = ADC(Pin(26))

def lectura():
    valor_pot = adc.read_u16() /16 # Lee un valor de 0 a 65535
    voltaje = valor_pot / 4  # Convierte el valor a voltaje
    print(int(valor_pot))
    
tim = Timer()
tim.init(freq=100000, mode=Timer.PERIODIC, callback=lambda t:lectura())
    
    
while True:
    pass
    
