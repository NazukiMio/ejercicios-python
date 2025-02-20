dia=input("Por favor, ingrese un numero del dia de la semana: ")
semana=[1,2,3,4,5,6,7]
if dia in semana:
    if dia==1:
        print("Lunes")
    elif dia==2:
        print("Martes")
    elif dia==3:
        print("Miercoles")
    elif dia==4:
        print("Jueves")
    elif dia==5:
        print("Viernes")
    elif dia==6:
        print("Sabado")
    elif dia==7:
        print("Domingo")
else:
    print("Numero esta fuera del rango")