from funciones import *

# def informar_resultados(numero_uno:int,numero_dos:int,lista_resultados:list) -> None:
#     print("ESTA FORMA DE INFORMAR RESULTADOS LA VAMOS A HACER CUANDO VEAMOS LISTAS")

def informar_resultados(numero_uno:int,numero_dos:int) -> None:
    resultado_suma = calcular_suma(numero_uno,numero_dos)
    resultado_resta = calcular_resta(numero_uno,numero_dos)
    resultado_division = calcular_division(numero_uno,numero_dos,"Error, no se puede dividir por cero")
    resultado_multiplicacion = calcular_multiplicacion(numero_uno,numero_dos)
    resultado_potencia = calcular_potencia(numero_uno,numero_dos)
    factorial_uno = calcular_factorial(numero_uno)
    factorial_dos = calcular_factorial(numero_dos)
    
    informar_resultado(numero_uno,numero_dos,resultado_suma,"+")
    informar_resultado(numero_uno,numero_dos,resultado_resta,"-")
    informar_resultado(numero_uno,numero_dos,resultado_multiplicacion,"*")
    informar_resultado(numero_uno,numero_dos,resultado_division,"/")
    informar_resultado(numero_uno,numero_dos,resultado_potencia,"elevado a ")
    informar_factorial(numero_uno,numero_dos,factorial_uno,factorial_dos)

def informar_resultado(numero_uno:int,numero_dos:int,resultado:int | float | str,operador:str) -> None:
    if type(resultado) == float:
        print(f"{numero_uno} {operador} {numero_dos} = {resultado:.2f}")
    else:
        print(f"{numero_uno} {operador} {numero_dos} = {resultado}")

def informar_factorial(numero_uno:int,numero_dos:int,resultado_1:int | float | str,resultado_2:int | float | str) -> None:
    print(f"{numero_uno}! = {resultado_1}")
    print(f"{numero_dos}! = {resultado_2}")