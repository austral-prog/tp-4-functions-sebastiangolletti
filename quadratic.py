import math


def roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"({x1}, {x2})"
    elif delta == 0:
        x = -b / (2*a)
        return f"({x})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    partes = []

    if a != 0:
        partes.append(f"{a} * X^2")

    if b != 0:
        partes.append(f"{b} * X")

    if c != 0:
        partes.append(f"{c}")

    if not partes:
        return "f(x) = 0"

    return "f(x) = " + " + ".join(partes)


def derivation(a, b, c):
    partes = []

    if a != 0:
        partes.append(f"{2*a} * X")

    if b != 0:
        partes.append(f"{b}")

    if not partes:
        return "f'(x) = 0"

    return "f'(x) = " + " + ".join(partes)
