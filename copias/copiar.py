with open("origen.txt", "r") as origen:
    contenido = origen.read()

with open("destino.txt", "w") as destino:
    destino.write(contenido)

print("El contenido de 'origen.txt' ha sido copiado a 'destino.txt'.")
