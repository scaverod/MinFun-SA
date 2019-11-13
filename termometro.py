# Temperaturas usadas
from math import e, cos, sin, tan, tanh, log


# Temepratura estática en la que referencia a Kirkpatric 1985, no encuentro el paper
def temperatura_kirkpatrick(iteracion, descanso, temperatura_actual, alpha, temperatura_inicial):
    if iteracion % descanso == 0:
        temperatura = alpha ** (iteracion / descanso) * temperatura_inicial
    else:
        temperatura = float(temperatura_actual)
    return max(0.01, min(1, temperatura))


def temperatura_lundy(temperatura, beta):
    return max (0.01, temperatura / (1 + beta * temperatura))


def temperatura_hajek(iteracion, constante):
    return constante / log(iteracion + 1)


def temperatura_adicional(estado):
    return max(0.01,  1 - estado)


def beta_lundy(temperatura_inicial, temperatura_final, n_entornos):
    return (temperatura_inicial - temperatura_final) / (n_entornos * temperatura_inicial * temperatura_final)