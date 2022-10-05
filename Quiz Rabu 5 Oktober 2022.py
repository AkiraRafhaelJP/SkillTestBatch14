import math

while True:
    try:
        n = int(input('Masukkan input: '))
        print(f'Nilai {n}! = {math.factorial(n)}')
        break
    except ValueError as ve:
        print(f'Input tidak valid. Masukkan input (bilangan bulat) lain!\n')
    