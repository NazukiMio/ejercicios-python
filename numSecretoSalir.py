import random

numero_secreto= random.randint(1,20)

while True:
    numero_usuario = input('Ingrese un número del 1 al 20 o "salir" para terminar: ')
    if numero_usuario.lower() == "salir":
        print(f"El numero secreto es {numero_secreto}")
        break
    try:
        numero_usuario = int(numero_usuario)
        if numero_usuario == numero_secreto:
            print("Ganaste")
            break
    except ValueError:
        print("Por favor ingrese un número entero o 'salir'")
        continue
