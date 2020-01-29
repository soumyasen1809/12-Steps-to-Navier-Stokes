from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the parameters
x_max = 2   # Domain length in X
y_max = 2   # Domain length in Y
x_points = 101   # Number of grid points in X
y_points = 101   # Number of grid points in Y
t_points = 80  # Number of time steps
del_x = x_max/float(x_points - 1)
del_y = y_max/float(y_points - 1)
del_t = 0.2*del_x

x = np.linspace(0, x_max, x_points)
y = np.linspace(0, y_max, y_points)

u = np.ones((x_points,y_points))
v = np.ones((x_points,y_points))
for i in range(0, x_points):    # Specifying the boundary conditions
    for j in range(0, y_points):
        if x[i] > 0.5 and x[i] < 1.0:
            if y[j] > 0.5 and y[j] < 1.0:
                u[i,j] = 2.0
                v[i, j] = 2.0

# Looping for time steps
u_new = np.ones((x_points, y_points))
v_new = np.ones((x_points, y_points))

for it in range(0, t_points):
    for ix in range(1, x_points):
        for iy in range(1, y_points):
            u_new[ix, iy] = u[ix, iy] - u[ix, iy] * (del_t / float(del_x)) * (u[ix, iy] - u[ix - 1, iy]) - v[ix, iy] * (
                        del_t / float(del_y)) * (u[ix, iy] - u[ix, iy - 1])
            u_new[0,:] = 1.0
            u_new[:,-1] = 1.0
            u_new[-1,:] = 1.0
            u_new[:,0] = 1.0

            v_new[ix, iy] = v[ix, iy] - u[ix, iy] * (del_t / float(del_x)) * (v[ix, iy] - v[ix - 1, iy]) - v[ix, iy] * (
                        del_t / float(del_y)) * (v[ix, iy] - v[ix, iy - 1])
            v_new[0, :] = 1.0
            v_new[:, -1] = 1.0
            v_new[-1, :] = 1.0
            v_new[:, 0] = 1.0

    u = u_new.copy()
    v = v_new.copy()

# Plotting the 2D surface
fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
fig.suptitle("Solution of u ")
plt.show()

fig = plt.figure()
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X, Y, v[:], cmap=cm.viridis)
fig.suptitle("Solution of v ")
plt.show()
