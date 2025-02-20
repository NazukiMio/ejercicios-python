def promedio(*args):
    try:
        if not args:
            return "No se ingresaron numeros"
        else:
            return sum(args)/len(args)
    except TypeError:
        return "Error: No se puede procesar la entrada actual"
    
lista = input("Ingrese una lista de numeros separados por comas: ").split(",")

try:
    lista = [float(x) for x in lista]
except ValueError:
    print("Error: La lista contiene elementos no numericos o hay un campo vacio")

print(promedio(*lista))
    