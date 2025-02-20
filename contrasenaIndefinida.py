contrasena_correcta = "python123"
contrasena = input("Ingrese su contraseña: ")

while True:
    if contrasena == contrasena_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        contrasena = input("Ingrese su contraseña: ")
