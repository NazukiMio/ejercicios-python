cadena = "Hola a todos"
#print(cadena.replace(" ", ""))
#Usa bucle
for i in cadena:
    if i != " ":
        print(i, end="")
    else:
        print("", end="")