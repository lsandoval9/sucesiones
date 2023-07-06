import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=15) # Configuramos la precisión de los decimales

def primera_sucesion(n: int = 10):
    x = np.zeros(n+1) # Inicializamos el arreglo x con ceros

    x[0] = 0.99996
    for i in range(1, n+1):
        x[i] = (1/3) * x[i - 1]
    return x

def graficar_primera_sucesion(n: np.ndarray):
    plt.plot(n, '.')
    plt.title('sucesion (1/3)*r_{n-1}')
    plt.grid(True)
    plt.xlabel('n')
    plt.show()

def imprimir_con_indices(n: np.ndarray):
    for i in range(1, len(n)):
        np.set_printoptions(suppress=True, precision=30)
        print(i, n[i])

#graficar_primera_sucesion(primera_sucesion(10))
#imprimir_con_indices(primera_sucesion(10))