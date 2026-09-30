def calcular_suma(numero_a : int ,numero_b : int) -> int:#Definición
    """Se encarga de sumar dos numeros enteros

    Args:
        numero_a (int): El primer numero a sumar
        numero_b (int): El segundo numero a sumar

    Returns:
        int: El resultado de la suma correspondiente
    """

    resultado = numero_a + numero_b
    return resultado

def calcular_resta(numero_a : int ,numero_b : int) -> int:
    """Se encarga de restar dos numeros enteros

    Args:
        numero_a (int): El primer numero a restar
        numero_b (int): El segundo numero a restar

    Returns:
        int: El resultado de la resta correspondiente
    """

    resultado = numero_a - numero_b
    return resultado

def calcular_multiplicacion(numero_a : int ,numero_b : int) -> int:
    """Se encarga de calcular el producto de dos numeros enteros

    Args:
        numero_a (int): El primer numero a multiplicar
        numero_b (int): El segundo numero a multiplicar

    Returns:
        int: El resultado del producto correspondiente
    """

    resultado = numero_a * numero_b
    return resultado

def calcular_potencia(base : int ,exponente : int) -> int:
    """Se encarga de calcular una potencia entre numeros enteros

    Args:
        base (int): Base de la potencia
        exponente (int): Exponente de la potencia

    Returns:
        int: El resultado de la potencia correspondiente
    """

    resultado = base ** exponente
    return resultado

def calcular_division(dividendo:int , divisor:int, mensaje_error : str = "ERROR") -> float | str:
    """Calcula la division entre dos numeros

    Args:
        dividendo (int): Dividendo de la division
        divisor (int): Divisor de la division
        mensaje_error (str, optional): El mensaje de error correspondiente al resultado por division por cero. por defecto es "ERROR".

    Returns:
        float | str: Resultado de la division o en caso de error un mensaje
    """
    if divisor != 0:
        resultado = dividendo / divisor
    else:
        resultado = mensaje_error

    return resultado

def calcular_factorial(numero:int,mensaje_error:str = "ERROR") -> int | str:
    if numero == 0 or numero == 1:
        resultado_factorial = 1
    elif numero > 1:
        resultado_factorial = numero * calcular_factorial(numero - 1)
    else:
        resultado_factorial = mensaje_error

    return resultado_factorial

def calcular_todas_operaciones(lista_operaciones:list) -> list:
    print("DESARROLLAMOS CUANDO VEAMOS LISTAS")

