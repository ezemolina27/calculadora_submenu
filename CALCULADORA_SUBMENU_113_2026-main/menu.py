import time
import platform
import subprocess
from funciones import *
from salidas import *
from entradas import *

def limpiar_consola() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls",shell=True)
        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear",shell=True)
        subprocess.run("clear",shell=True)

def refrescar_menu(tiempo_menu:int = 0,mensaje_menu:str = "Toque enter para continuar...", ) -> None:
    time.sleep(tiempo_menu)
    if tiempo_menu == 0:
        input(mensaje_menu)
    limpiar_consola()

def mostrar_menu_calculadora() -> None:
    print("\nMENU PRINCIPAL CALCULADORA\n")
    print("1. Ingresar el primer numero")
    print("2. Ingresar el segundo numero")
    print("3. Calcular")
    print("4. Salir")

def mostrar_submenu_calculadora() -> None:
    print("\nSUBMENU CALCULADORA\n")
    print("1. Calcular la suma")
    print("2. Calcular la resta")
    print("3. Calcular la division")
    print("4. Calcular la multiplicacion")
    print("5. Calcular la potencia")
    print("6. Calcular el factorial")
    print("7. Calcular todos los resultados")
    print("8. Salir")

def ejecutar_menu_principal_calculadora() -> None:
    bandera_primer_numero = False
    bandera_segundo_numero = False

    while True:
        mostrar_menu_calculadora()
        opcion = pedir_entero_rango(1,4,"Ingrese una opcion en el menu: ","ERROR, la opcion tiene que estar entre (1 y 4)")
        limpiar_consola()

        if opcion == 1:
            numero_uno = int(input("Ingrese el primer numero: "))
            bandera_primer_numero = True
        elif opcion == 2:
            numero_dos = int(input("Ingrese el segundo numero: "))
            bandera_segundo_numero = True
        elif opcion == 3 and bandera_primer_numero == True and bandera_segundo_numero == True:
            ejecutar_sub_menu_calculadora(numero_uno,numero_dos)
        elif opcion == 4:
            print("SALIENDO DEL PROGRAMA")
            break
        else:
            print("NO SE PUEDE ACCEDER A LA OPCION 3 SIN ANTES CARGAR LOS NUMEROS")

        refrescar_menu()

def ejecutar_sub_menu_calculadora(numero_uno:int, numero_dos: int) -> None:
    while True:
        mostrar_submenu_calculadora()
        opcion = pedir_entero_rango(1,8,"Ingrese una opcion en el menu: ","ERROR, la opcion tiene que estar entre (1 y 4)")
        limpiar_consola()

        if opcion == 1:
            resultado_suma = calcular_suma(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_suma,"+")
        elif opcion == 2:
            resultado_resta = calcular_resta(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_resta,"-")
        elif opcion == 3:
            resultado_division = calcular_division(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_division,"/")
        elif opcion == 4:
            resultado_multiplicacion = calcular_multiplicacion(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_multiplicacion,"*")
        elif opcion == 5:
            resultado_potencia = calcular_potencia(numero_uno,numero_dos)
            informar_resultado(numero_uno,numero_dos,resultado_potencia,"elevado a ")
        elif opcion == 6:
            factorial_1 = calcular_factorial(numero_uno)
            factorial_2 = calcular_factorial(numero_dos)
            informar_factorial(numero_uno,numero_dos,factorial_1,factorial_2)
        elif opcion == 7:
            informar_resultados(numero_uno,numero_dos)
        elif opcion == 8:
            print("SALIR")
            break

        refrescar_menu()

def interactuar_menu(lista_datos:list) -> bool:
    print("EN DESARROLLO CUANDO VEAMOS LISTAS")