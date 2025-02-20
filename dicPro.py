productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
print("Producto y precio: ")
for pro, pre in productos.items():
    print(pro, pre)
print("Total: ")
total = sum(productos.values())
print(total)
print("Productos con precio mayor a: ")
valor_1 = float(input("Ingrese el valor: "))
productos_caros = [pro for pro, pre in productos.items() if pre > valor_1]
print(f"Los productos con precio mayor a {valor_1} son: {productos_caros}")