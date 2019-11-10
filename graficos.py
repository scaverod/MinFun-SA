import numpy as np
import matplotlib.pyplot as plt


def plot_results(funcion, fun_range, valores_x, valores_y, valores_t):
    funcion = np.vectorize(funcion)
    x_list = np.linspace(fun_range[0], fun_range[1], (fun_range[1] - fun_range[0]) * 4)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 15))
    fig.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.2)
    fig.suptitle('Resultados de la optimización')
    ax1.set_title('Función a optimziar')
    ax2.set_title('Evolución de la temperatura')
    ax3.set_title('Soluciones (Valores de x)')
    ax4.set_title('Calidad (Valores de y)')
    ax1.plot(x_list, funcion(x_list))
    ax1.plot(valores_x[-1], valores_y[-1], marker='*', markersize=5, color="black")
    ax2.plot(valores_t, 'tab:orange')
    ax3.plot(valores_x, 'tab:green')
    ax4.plot(valores_y, 'tab:red')
    print("Solución x: " + str(valores_x[-1]))
    print("Calidad de la solución x, f(x):" + str(valores_y[-1]))
