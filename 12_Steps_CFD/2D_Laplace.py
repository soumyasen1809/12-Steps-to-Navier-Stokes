import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

x_max = 2           # Max domain in X
y_max = 1           # Max domain in Y
x_points = 31       # Number of grid points in X
y_points = 31       # Number of grid points in Y
it_points = 100     # Number of iteration points
del_x = x_max/float(x_points - 1)
del_y = y_max/float(y_points - 1)

x = np.linspace(0, x_max, x_points)
y = np.linspace(0, y_max, y_points)

p = np.zeros((x_points, y_points))  # Pressure = 0 at all points except boundary points
p[0,:] = 0       # Dirichlet boundary condition p = 0 at x = 0
p[-1,:] = y      # Dirichlet boundary condition p = y at x = 2
p[:, 0] = p[:, 1]   # Neuman boundary condition dp/dy = 0 at y = 0
p[:, -1] = p[:, -2] # Neuman boundary condition dp/dy = 0 at y = 1

# Loop through iterations
p_new = np.zeros((x_points, y_points))
for it in range(0, it_points):
    for ix in range(1, x_points - 1):
        for iy in range(1, y_points - 1):
            p_new[ix, iy] = (del_y ** 2 * (p[ix + 1, iy] + p[ix - 1, iy]) + del_x ** 2 * (
                        p[ix, iy + 1] + p[ix, iy - 1])) / (float(2) * (del_x ** 2 + del_y ** 2))

            p_new[0, :] = 0  # Dirichlet boundary condition p = 0 at x = 0
            p_new[-1, :] = y  # Dirichlet boundary condition p = y at x = 2
            p_new[:, 0] = p[:, 1]  # Neuman boundary condition dp/dy = 0 at y = 0
            p_new[:, -1] = p[:, -2]  # Neuman boundary condition dp/dy = 0 at y = 1

    p = p_new.copy()

# Plotting pressure p
fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, p[:], cmap=cm.viridis)
plt.show()
