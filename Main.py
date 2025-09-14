#Main.py

from ABML import * 

def main():
    opcion = ""
    
    while opcion != "7":
        print("=== GESTOR DE TURNOS ===")
        print("1. Alta cliente")
        print("2. Modificacion")
        print("3. Eliminacion")
        print("4. Listado General")
        print("5. Consulta por Cliente")
        print("6. Consulta por Fecha")
        print("7. Salir del Programa")
        
        opcion = input("Seleccione una opcion: ") 

        if opcion == "1":
            altaCliente()
        elif opcion == "2":
            print("Función de modificación aún no implementada")
        elif opcion == "3":
            print("Función de eliminación aún no implementada")
        elif opcion == "4":
            ListadoClientes()
        elif opcion == "5":
            print("Función de consulta por cliente aún no implementada")
        elif opcion == "6":
            print("Función de consulta por fecha aún no implementada")
        elif opcion == "7":
            print("Saliendo...")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
