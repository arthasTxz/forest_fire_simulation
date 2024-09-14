import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Crear figuras y ejes para dos gráficos
fig, (ax1, ax2) = plt.subplots(2, 1)

# Datos iniciales
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Líneas que se animarán
line1, = ax1.plot(x, y1, color='r')
line2, = ax2.plot(x, y2, color='b')

# Función de actualización para la animación
def update(frame):
    line1.set_ydata(np.sin(x + frame / 10))
    line2.set_ydata(np.cos(x + frame / 10))
    return line1, line2

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

plt.show()

