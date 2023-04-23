import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Definir el tamaño de la placa
# hola ferrrr
Lx, Ly, Lz = 1, 1, 0.01

# Crear la malla de puntos X e Y
Nx, Ny = 50, 50
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Definir la velocidad de sonido en la placa
E = 2.0e11  # Modulo de elasticidad en N/m^2
nu = 0.3  # Coeficiente de Poisson
rho = 7800  # Densidad en kg/m^3
c = np.sqrt(E/(rho*(1 - nu**2)))  # Velocidad de propagacion en m/s

# Crear la figura y el objeto Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # type: ignore

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Definir una función para crear la superficie de Chladni
def create_chladni_surface(f):
    # Calcular el número de onda
    omega = 2*np.pi*f
    k = omega/c

    # Crear la matriz Z con los valores de la frecuencia
    Z = np.sin(k*X) * np.sin(k*Y)

    # Graficar la superficie
    ax.clear()
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

    # Configurar el título de la figura
    ax.set_title('Patrón de Chladni para f = {} Hz'.format(f))

# Crear una animación que muestre el patrón de Chladni a medida que varía la frecuencia
freqs = np.linspace(20, 20000, 60)  # Frecuencias de 500 a 6000 Hz
ani = FuncAnimation(fig, create_chladni_surface, frames=freqs, repeat=True)

# Mostrar la animación
plt.show()
