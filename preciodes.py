precio=int(input("Ingrese el precio: "))
descuento=precio*0.10
preciofinal=precio-descuento

if precio>1000:
    print("Tiene un descueto, el precio final es: ", preciofinal)
else:
    print("El precio final es: ", precio)