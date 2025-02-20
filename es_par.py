def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

num=int(input("Ingrese un numero: "))

print(es_par(num))