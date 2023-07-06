


from matplotlib import pyplot as plt
import numpy as np

from primera import primera_sucesion
from segunda import segunda_sucesion
from tercera import tercera_sucesion

np.set_printoptions(suppress=True)


def graficar_sucesiones():
    x = primera_sucesion(100)
    y = segunda_sucesion(100)
    #print("resta:",xy)
    z = tercera_sucesion(100)
    plt.plot(x, '.', label='(1/3)*r_{n-1}')
    plt.plot(y, '.', label='(4/3)*r_{n-1} - (1/3)*r_{n-2}')
    plt.plot(z, '.', label='(10/3)*r_{n-1} - r_{n-2}')

    #plt.plot(xy, '.', label='(1/3)*r_{n-1} - (4/3)*r_{n-1} + (1/3)*r_{n-2}')

    plt.title('sucesion (10/3)*r_{n-1} - r_{n-2}')
    plt.grid(True)
    plt.xlabel('n')
    plt.legend()
    plt.show()

graficar_sucesiones()