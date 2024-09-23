import time

# def bit_length(n):
#     bits = 0
#     while n:
#         bits += 1
#         n >>= 1
#     return bits

# def get_msb_and_next_four_bits(number):
#     num_bits = bit_length(number)
#     next_four_bits = (number >> max(0, num_bits - 5)) & 0b1111 if num_bits > 1 else 0
#     return num_bits, next_four_bits

# def create_comprimed_number(msb, next_four_bits):
#     msb_minus_4 =  max(0,msb - 4)  # Ensure the result is not negative
#     return (msb_minus_4 << 4) | next_four_bits

# def compresed(number):
#     msb, next_four_bits = get_msb_and_next_four_bits(number)
#     comprimed8bits = create_comprimed_number(msb, next_four_bits)
#     return comprimed8bits

# contador_values = [5, 158, 301, 619, 1212, 3999, 5684, 9595, 16000, 32768, 62301]

# for contador in range(0, 65536):
#     print("Numero ingresado:", contador)
#     comprimed8bits = compresed(contador)
#     print("Numero comprimido:", comprimed8bits)
   
def alternative_bit_length(n):
    bits = 0
    while n:
        bits += 1
        n >>= 1
    return bits

def compresed(number):
    msb = alternative_bit_length(number)
    next_four_bits = (number >> max(0, msb - 5)) & 0b1111 if msb > 1 else 0
    msb_minus_4 = max(0, msb - 4)
    comprimed8bits = (msb_minus_4 << 4) | next_four_bits
    return comprimed8bits

contador_values = [5, 158, 301, 619, 1212, 3999, 5684, 9595, 16000, 32768, 62301]

for contador in contador_values:
    print("Numero ingresado:", contador, "en binario:", bin(contador))
    comprimed8bits = compresed(contador)
    print("Numero comprimido:", comprimed8bits, "en binario:", bin(comprimed8bits))
    print("-------------------------")
    time.sleep(0.00001)