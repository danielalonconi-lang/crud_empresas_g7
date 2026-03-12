from time import sleep
from src.datos import empresas,guardar_datos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresas():
    ruc = input("INGRESE RUC : ")
    razon_social = input("INGRESE SU RAZON SOCIAL : ")
    direccion = input("INGRESE DIRECCIÓN : ")
    
    empresas[ruc] = {
        "razon_social":razon_social,
        "direccion":direccion
    }
    titulo("SU EMPRESA FUE REGISTRADA DE MANERA SATISFACTORIA")
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_empresas():
    for ruc,info in empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON_SOCIAL : {info['razon_social']}")
        print(f"DIRECCIÓN : {info['direccion']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR EMPRESA")
def actualizar_empresa():
    ruc = input("Ingrese RUC de la empresa : ")

    if ruc in empresas:
        print(f"Empresa encontrada : {empresas[ruc]['razon_social']}")
        print("Ingrese nuevos datos o presione ENTER para conservar los anteriores")

        nuevo_razonsocial = input(f"Nueva razon social ({empresas[ruc]['razon_social']}): ")
        nuevo_direccion = input(f"Nueva dirección ({empresas[ruc]['direccion']}): ")

            
        empresas[ruc]["razon_social"] = nuevo_razonsocial if nuevo_razonsocial else empresas[ruc]["razon_social"]

        if nuevo_direccion != "":
            empresas[ruc]["direccion"] = nuevo_direccion
        print("Empresa actualizada...")
    else:
        print("Su empresa no fue encontrada...")
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresa():
    ruc = input("Ingrese RUC de la empresa : ")
    
    if ruc in empresas:
        del empresas[ruc]
        print("Su empresa fue eliminada satisfactoriamente!")
    else:
        print("Su empresa no fue encontrada...")
        
def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESA
            [2] MOSTRAR EMPRESA
            [3] ACTUALIZAR EMPRESA
            [4] ELIMINAR EMPRESA
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_empresas()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresa()
            pausa()
        elif opcion == 4:
            eliminar_empresa()
            pausa()
        elif opcion == 5:
            guardar_datos(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("Datos guardados en empresas.csv")
            sleep(2)
            break
        else:
            print("Opción no válida.")