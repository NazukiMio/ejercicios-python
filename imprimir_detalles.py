def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

diccionario={}

print("Ingrese clave y valor de forma alternada (escriba 'ya estan todos' en cualquier momento para terminar):")

while True:
    clave = input("Ingrese clave: ")
    if clave == "ya estan todos":
        break
    valor = input("Ingrese valor: ")
    if valor == "ya estan todos":
        break
    diccionario[clave.strip()] = valor.strip()

imprimir_detalles(**diccionario)