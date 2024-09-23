import time

def extract_bits(number):
    location = number >> 4
    information = number & 0b1111
    if location > 0:
        location = location + 3
        print("location:", location)
        return (1 << location) | (information << (location - 4))
    else:
        return information

contador_values = [5, 67, 82, 99, 114, 143, 150, 162, 175, 192, 206]

for contador in contador_values:
    print("Numero ingresado:", contador, "en binario:", bin(contador))
    data = extract_bits(contador)
    print("Data:", data, "en binario:", bin(data))
    print("-------------------------")
    time.sleep(0.001)