num = int(input("Ingrese un numero: "))
resulta = 1
while num > 0:
    resulta *= num
    num -= 1
print(f"El factorial de {num} es {resulta}")