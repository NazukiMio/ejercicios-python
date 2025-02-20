nombres = []

while True:
    nombre = input("Ingresa un nombre (o escribe 'ya estan todos' para terminar): ")
    if nombre.lower() == 'ya estan todos':
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as nombres_archivo:

    for nombre in nombres:
        nombres_archivo.write(nombre + "\n")

print("Los nombres han sido guardados en nombres.txt.")

with open("nombres.txt","r") as contenidos:
    contenido=contenidos.read()
    print(contenido)