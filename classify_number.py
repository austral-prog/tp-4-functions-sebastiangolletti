# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    if n % 2 == 0:
        return "True"
    else:
        return "False"


def is_positive(n):

    if n > 0:
        return "True"
    else:
        return "False"


def classify_number(n):
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive para resolver el ejercicio.

    Clasificaciones posibles:
      - "positive even"   (positivo y par)
      - "positive odd"    (positivo e impar)
      - "negative even"   (negativo y par)
      - "negative odd"    (negativo e impar)
      - "zero"            (el número es 0)
    """
    if n > 0 and n % 2 == 0:
        return "positive even"
    if n > 0 and n % 2 == 1:
        return "positive odd"
    if n < 0 and n % 2 == 0:
        return "negative even"
    if n < 0 and n % 2 == 1:
        return "negative odd"
    if n == 0:
        return "zero"


