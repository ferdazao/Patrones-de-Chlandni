import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir el tamaño de la placa
Lx, Ly, Lz = 1, 1, 0.01

# Crear la malla de puntos X e Y
Nx, Ny = 50, 50
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Crear la matriz Z con los valores de la frecuencia
f = 5640  # Frecuencia en Hz 1397, 5640
k = 2*np.pi*f
Z = np.sin(k*X) * np.sin(k*Y)

# Crear la figura y el objeto Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # type: ignore

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Patrón de Chladni para f = {} Hz'.format(f))

# Mostrar la figura
plt.show()
