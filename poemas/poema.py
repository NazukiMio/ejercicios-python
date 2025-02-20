with open('poema.txt', 'r') as poema:
    lineas = poema.readlines()

print(f'El archivo poema.txt tiene {len(lineas)} líneas.')
