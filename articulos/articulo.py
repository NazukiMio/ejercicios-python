def contar_palabra(archivo, palabra):
    with open("articulo.txt", 'r') as articulo:
        contenido = articulo.read().lower()
    return contenido.count(palabra.lower())

palabra = input("Ingrese la palabra que desea buscar: ")

apariciones = contar_palabra("articulo.txt", palabra)

print(f'La palabra "{palabra}" aparece {apariciones} veces en el archivo.')
