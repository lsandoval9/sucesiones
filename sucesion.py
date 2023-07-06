import numpy as np
import matplotlib.pyplot as plt
# TODO: Implementar la función sucesion(n) que devuelve un arreglo con los n primeros términos de la sucesión
np.set_printoptions(precision=15) # Configuramos la precisión de los decimales

def sucesion(n: int):
    x = np.zeros(n+1) # Inicializamos el arreglo x con ceros
    for i in range(0, n+1):
        x[i] = 1 / (3 ** i)
    return x

def graficar(n: np.ndarray):
    plt.plot(n, '.')
    plt.title('sucesion (10/3)*r_{n-1} - r_{n-2}')
    plt.grid(True)
    plt.xlabel('n')
    plt.show()

def imprimir_con_indices(n: np.ndarray):
    for i in range(0, len(n) - 1):
        np.set_printoptions(suppress=True, precision=30)
        print(i, n[i])


#imprimir_con_indices(sucesion(10))
# graficar(sucesion(10))