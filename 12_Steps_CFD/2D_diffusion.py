import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Defining the parameters
x_max = 2      # Length of domain in X
y_max = 2      # Length of domain in Y
x_points = 31  # Defining the number of grid points in X
y_points = 31  # Defining the number of grid points in Y
t_points = 15  # Defining the number of time steps
del_x = x_max/float(x_points - 1)
del_y = x_max/float(y_points - 1)
nu = 0.5       # Viscosity
del_t = 0.25*del_x*del_y/float(nu)

x = np.linspace(0, x_max, x_points)
y = np.linspace(0, y_max, y_points)

u = np.ones((x_points, y_points))
for i in range(0, x_points):
    for j in range(0, y_points):
        if x[i] > 0.5 and x[i] < 1.0:
            if y[j] > 0.5 and y[j] < 1.0:
                u[i,j] = 2.0

u_new = np.ones((x_points, y_points))

for nt in range(0, t_points + 1):
    for ix in range(1, x_points-1):
        for iy in range(1, y_points-1):
            u_new[ix, iy] = u[ix, iy] + (nu) * (del_t / float(np.power(del_x, 2))) * (
                        u[ix + 1,iy] - 2 * u[ix,iy] + u[ix - 1,iy]) + (nu) * (del_t / float(np.power(del_y, 2))) * (
                                        u[ix,iy + 1] - 2 * u[ix,iy] + u[ix,iy - 1])

            u_new[0,:] = 0
            u_new[:, 0] = 0
            u_new[-1, :] = 0
            u_new[:, -1] = 0

    u = u_new.copy()

# Plot for different time steps
fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis, antialiased = False)
plt.show()
