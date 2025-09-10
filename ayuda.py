import csv

def agregar():
    with open("productos.csv", "a", newline="") as file:
        writer = csv.writer(file)
        id_producto = input("Ingrese el id del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        writer.writerow([id_producto, nombre, precio, 1])


def Listar():
    with open("productos.csv", "r") as file:
        next(file) #Saltar cabezera
        #reader = file.readlines()
        reader = csv.reader(file)
        for row in reader:
            if row[3] == "1":
                print(row)


def Actualizar():

    print("actualizando xd")
    
    productos = []

    id_buscar = input("Ingrese el id del producto a actualizar: ")
    nombre_nuevo = input("Ingrese el nuevo nombre del producto: ")
    precio_nuevo = input("Ingrese el nuevo precio del producto: ")

    actualizado = False
    with open("productos.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        encabezado = next(reader, None)
        for row in reader:
            productos.append(row)
            if row[0] == id_buscar:
                row[1] = nombre_nuevo
                row[2] = precio_nuevo
                actualizado = True
                
    
    with open("productos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)
        writer.writerows(productos)


    if actualizado:
        print("Producto actualizado con exito")
    else:
        print ("Producto no encontrado")

    


def Eliminar():
    print("eliminando xd")
    productos = []
    id_producto = input("Ingrese el id del producto a eliminar: ")
    eliminado = False
    with open("productos.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        encabezado = next(reader, None)
        
        for row in reader:
            productos.append(row)
            if row[0] == id_producto:
                row[3] = "0"
                eliminado = True
            
    
    with open("productos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)
        writer.writerows(productos)
    

    if eliminado:
        print("Producto eliminado con exito")
    else:
        print("Producto no encontrado")            



def menu():
    while True:
        print("\n--- MENU DE OPCIONES ---")
        print("1. Agregar un producto")
        print("2. Listar productos")
        print("3. Actualizr un producto")
        print("4. Eliminar un producto")
        print("5. Salir")

        op = input("Seleccione una opcion: ")

        if op == "1":
            agregar()
        elif op == "2":
            Listar()
        elif op == "3":
            Actualizar()
        elif op == "4":
            Eliminar()
        elif op == "5":
            exit()
        else:
            print("Opcion no valida")


menu()