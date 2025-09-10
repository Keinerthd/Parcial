import csv

def ordenamientoBurbujaConDislexia():
    with open("libros.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            print("hmm")


def librosOrdenados():
    print("\n--- LISTANDO LIBROS POR AÑO DE PUBLICACION ---")

    menor = False
    a = 0
    with open("libros.csv", "r") as f:
        read = csv.reader(f)

        for row in read:
            a = row[4]
            for row in read:
                b = row[4]    
                if a > b:
                     print(row)
                    







def Agregar():
    print("\n--- AGREGANDO NUEVO USUARIO ---")
    usuario = []
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese su correo electronico: ")
    id = 0

    with open("usuarios.csv", "r") as f:
        reader = csv.reader(f)
        encabezado = next(reader,None)
        for row in reader:
            id = max(row[0]) 


    with open("usuarios.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([int(id) + int(1), nombre, email])


   

def totalPrestamos():
    print("\n--- CALCULANDO TOTAL DE PRESTAMOS POR LIBRO ---")


    with open("libros.csv" ,"r") as f:
        reader = csv.reader(f)
        encabezado = next(reader, None)

        
        for row in reader:
            libro_id = row[2]
            cantidad = row[3]
            titulo = row[1]
        
        for row in reader:
            if libro_id == row[2]:
                total_prestamos = total_prestamos + cantidad

                   

    with open("total_prestamos.csv", "a",newline="") as f:
        totalLibros = []
        writer = csv.writer(f)
        writer.writerow([libro_id, titulo, total_prestamos])



    with open("prestamos.csv", "r") as f:
        reader = csv.reader(f)


def VerUsuariosPrestamos():
    print("\n--- VIENDO USUARIOS POR PRESTAMOS ---")

    with open("usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            id = row[0]
    
    
    with open("prestamos.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if id == row[1]:
                if row[3] >= "1":
                    print(row)
    
    with open("prestamos.csv", "w") as f:
        writer = csv.writer(f)
        print(row)






def menu():
    while True:
        print("\n ---- MENU ----")
        print("1. Ver libros ordenados por año de publicacion")
        print("2. Agregar un nuevo usuario")
        print("3. Calcular total de prestamos por libro")
        print("4. Ver usuarios que han realizado prestamos")
        print("5. Salir")

        op = input("Seleccione una opcion: ")
        

        if op == "1":
            librosOrdenados()
        elif op =="2":
            Agregar()
        elif op =="3":
            totalPrestamos()
        elif op =="4":
            VerUsuariosPrestamos()
        elif op=="5":
            exit()

menu()