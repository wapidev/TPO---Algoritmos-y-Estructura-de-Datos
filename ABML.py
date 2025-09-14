from LibreriaPersonal import *

nombre = ""
telefono = ""
dni = ""
email = ""
estado = True

clientes_dd= { 
        "nombre": nombre,
        "telefono": telefono,
        "dni": dni,
        "email": email,
        "estado": estado
    } 

def altaCliente():
    tiposIndice(1)
    nombre = input("Nombre del cliente: ")
    telefono = input("Telefono: ")
    dni = input("DNI: ")
    email = input("Email: ")
    
    clientes_dd["nombre"] = nombre
    clientes_dd["telefono"] = telefono
    clientes_dd["dni"] = dni
    clientes_dd["email"] = email

    print("Cliente registrado correctamente.")
    tiposIndice(2)

def Listadoclientes():
    tiposIndice(1)
    print("=== LISTADO DE clientes_dd ===")
    
    if len(clientes_dd["nombre"]) == 0:
        print("No hay clientes_dd Registrados")
        
    else:
        for cliente in clientes_dd:
            print(f"| DNI: {cliente["dni"]} | Nombre: {cliente["nombre"]}  | Telefono: {cliente["telefono"]}  | Email: {cliente["email"]}  ")

    esperarTecla()
    tiposIndice(2)