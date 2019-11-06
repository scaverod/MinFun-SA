# En esta clase hay una recopilación de funciones
from math import e, cos, sin, tan, tanh, log


def exponencial(x, base=e):
    return base ** x


def potencia(x, exponente=2):
    return x ** exponente


def abs(x):
    return x * ((x < 0) * (-1) + (x > 0))


def seno(x):
    return sin(x)


def coseno(x):
    return cos(x)


def tangente(x):
    return tan(x)


def tangente_hipervolica(x):
    return tanh(x)


def logaritmo(x, base=e):
    return log(x, base)


def funcion_enunciado(x):
    return coseno(x) / x


def funcion_curiosa_1(x):
    return logaritmo(potencia(x, 9)) * seno(x)


def ajustar_valor(x, intervalo):
    return max(min(x, intervalo[1]), intervalo[0])
