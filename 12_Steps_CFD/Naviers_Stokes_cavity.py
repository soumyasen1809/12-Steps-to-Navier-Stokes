import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x_max = 2           # Max domain in X
y_max = 2           # Max domain in Y
x_points = 50       # Number of grid points in X
y_points = 50       # Number of grid points in Y
t_points = 100      # Number of time steps
it_points = 10     # Number of iteration points
del_x = x_max/float(x_points - 1)
del_y = y_max/float(y_points - 1)
del_t = 0.001       # Time step
rho = 1             # Density
nu = 0.1            # Viscosity

x = np.linspace(0, x_max, x_points)
y = np.linspace(0, y_max, y_points)

p = np.zeros((x_points, y_points))  # Pressure = 0 at all points except boundary points
u = np.zeros((x_points, y_points))
v = np.zeros((x_points, y_points))
b = np.zeros((x_points, y_points))      # RHS in Poisson's equation

# Loop through iterations
p_new = np.zeros((x_points, y_points))
u_new = np.zeros((x_points, y_points))
v_new = np.zeros((x_points, y_points))

for nt in range(0, t_points):
    for ix in range(1, x_points - 1):
        for iy in range(1, y_points - 1):
            for it in range(0, it_points):
                p_new[ix,iy] = (((p[ix + 1, iy] + p[ix - 1, iy]) * del_y ** 2 + (p[ix, iy + 1] + p[ix, iy - 1]) * del_x ** 2) / (float(2) * (del_x ** 2 + del_y ** 2)) - del_x ** 2 * del_y ** 2 / (float(2) * (del_x ** 2 + del_y ** 2)) * (rho * (1 / float(del_t) * ((u[ix + 1, iy] - u[ix - 1, iy]) / (float(2) * del_x) + (v[ix, iy + 1] - v[ix, iy - 1]) / (float(2) * del_y)) - ((u[ix + 1, iy] - u[ix - 1, iy]) / (float(2) * del_x)) ** 2 - 2 * ((u[ix, iy + 1] -u[ix - 1, iy]) / (float(2) * del_y) * (v[ix + 1, iy] -v[ix - 1, iy]) / (float(2) * del_x)) - ((v[ix, iy + 1] -v[ix, iy - 1]) / (float(2) * del_y)) ** 2)))

                p_new[-1, :] = p_new[-2, :]
                p_new[:, 0] = p_new[:, 1]
                p_new[0, :] = p_new[1, :]
                p_new[:, -1] = 0

            p = p_new.copy()

            u_new[ix, iy] = (u[ix, iy] - u[ix, iy] * del_t / float(del_x) * (u[ix, iy] - u[ix - 1, iy]) - v[
                ix, iy] * del_t / float(del_y) * (u[ix, iy] - u[ix, iy - 1]) - del_t / (float(2) * rho * del_x) * (
                                     p[ix + 1, iy] - p[ix - 1, iy]) + nu * (del_t / float(del_x ** 2) * (
                    u[ix + 1, iy] - 2 * u[ix, iy] + u[ix - 1, iy]) + del_t / float(del_y ** 2) * (
                                                                                    u[ix, iy + 1] - 2 * u[
                                                                                ix, iy] + u[ix, iy - 1])))

            v_new[ix, iy] = (v[ix, iy] - u[ix, iy] * del_t / float(del_x) * (v[ix, iy] - v[ix - 1, iy]) - v[
                ix, iy] * del_t / float(del_y) * (v[ix, iy] - v[ix, iy - 1]) - del_t / (float(2) * rho * del_y) * (
                                     p[ix, iy + 1] - p[ix, iy - 1]) + nu * (del_t / float(del_x ** 2) * (
                    v[ix + 1, iy] - 2 * v[ix, iy] + v[ix - 1, iy]) + del_t / float(del_y ** 2) * (
                                                                                    v[ix, iy + 1] - 2 * v[
                                                                                ix, iy] + v[ix, iy - 1])))

            u_new[0, :] = 0
            u_new[:, 0] = 0
            u_new[:, -1] = 0
            u_new[-1, :] = 1  # set velocity on cavity lid equal to 1

            v_new[0, :] = 0
            v_new[-1, :] = 0
            v_new[:, 0] = 0
            v_new[:, -1] = 0

        u = u_new.copy()
        v = v_new.copy()


# Plotting pressure p
fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()

fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, v[:], cmap=cm.viridis)
plt.show()

fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, p[:], cmap=cm.viridis)
plt.show()

fig = plt.figure()
plt.contourf(X,Y,p,alpha = 0.5, cmap = cm.viridis)
plt.colorbar()
plt.contour(X,Y,p,alpha = 0.5, cmap = cm.viridis)
plt.streamplot(X,Y,u,v)
plt.show()