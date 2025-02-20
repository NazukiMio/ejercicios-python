cadena = "Python es genial"
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print(f'In "Python es genial", tiene {contador} vocales')

