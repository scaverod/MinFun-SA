# Temperaturas usadas
from math import e, cos, sin, tan, tanh, log


# Temepratura estática en la que referencia a Kirkpatric 1985, no encuentro el paper
def temperatura_kirkpatrick(iteracion, descanso, temperatura_actual, alpha=0.95, temperatura_inicial=1):
    if iteracion % descanso == 0:
        temperatura = alpha ** (iteracion / descanso) * temperatura_inicial
    else:
        temperatura = float(temperatura_actual)
    return max(0.01, min(1, temperatura))


def temperatura_lundy(temperatura, beta):
    return temperatura / (1 + beta * temperatura)


def temperatura_hajek(iteracion, constante):
    return constante / log(iteracion + 1)
