import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=15) # Configuramos la precisión de los decimales

def tercera_sucesion(n: int = 10):
    x = np.zeros(n+1) # Inicializamos el arreglo x con ceros

    x[0] = 1
    x[1] = 0.33332
    for i in range(2, n+1):
        x[i] = ((10/3) * x[i - 1]) - ( x[i - 2])
    return x

def graficar_tercera_sucesion(n: np.ndarray):
    plt.plot(n, '.')
    plt.title('sucesion (10/3)*r_{n-1} - r_{n-2}')
    plt.grid(True)
    plt.xlabel('n')
    plt.show()

def imprimir_con_indices(n: np.ndarray):
    for i in range(1, len(n)):
        np.set_printoptions(suppress=True, precision=30)
        print(i - 1, n[i])
    


#imprimir_con_indices(tercera_sucesion(10))