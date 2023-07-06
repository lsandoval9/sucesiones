
from matplotlib import pyplot as plt
import numpy as np
from primera import primera_sucesion
from segunda import segunda_sucesion
from sucesion import sucesion
from tercera import tercera_sucesion




# graficar sucesion - primera

x = sucesion(11)
r = segunda_sucesion(10)

def graficar_sucesion(n: np.ndarray):
    plt.plot(n, '.')
    plt.title('sucesion x - r')
    plt.grid(True)
    plt.xlabel('n')
    plt.show()

def imprimir_con_indices(n: np.ndarray):
    for i in range(0, len(n) - 1):
        np.set_printoptions(suppress=True, precision=30)
        #valor absoluto de n[i]
        if np.abs(n[i]) < 0.1:
            #print(np.abs(n[i]))
            print(i, n[i])
