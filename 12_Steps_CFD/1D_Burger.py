import numpy as np
from matplotlib import pyplot as plt

x_max = 2     # Domain length in X
x_points = 101   # Number of grid points in X
t_points = 100   # Number of time steps
nu = 0.07        # Viscosity

del_x = x_max*np.pi/float(x_points - 1)   # Delta x (grid length)
del_t = del_x * nu    # Delta t (time interval)

x = np.linspace(0,x_max*np.pi,x_points)
u = np.ones(x_points)
u[0] = 0
u[- 1] = 0
# Defining boundary conditions
t = 0
for i in range(0, x_points):    # Initial condition of u
    u[i] = -2.0 * nu * (-(-8 * t + 2 * x[i]) * np.exp(-(-4 * t + x[i]) ** 2 / (float(4) * nu * (t + 1))) / (float(4) * nu * (t + 1)) \
                 - (-8 * t + 2 * x[i] - 4 * np.pi) * np.exp(-(-4 * t + x[i] - 2 * np.pi) ** 2 / (float(4) * nu * (t + 1))) / \
                 (float(4) * nu * (t + 1))) / (np.exp(-(-4 * t + x[i] - 2 * np.pi) ** 2 / (float(4) * nu * (t + 1))) + \
                                               np.exp(-(-4 * t + x[i]) ** 2 / (float(4) * nu * (t + 1)))) + 4

# Solve the linear 1D equation
u_new = np.ones(x_points)

for it in range(0, t_points):
    for ix in range(1, x_points-1):
        u_new[ix] = u[ix] - (u[ix])*(del_t/float(del_x))*(u[ix] - u[ix-1]) + (nu)*(del_t/float(np.power(del_x,2)))*(u[ix+1] - 2*u[ix] + u[ix-1])
        u_new[0] = u[0] - (u[0])*(del_t/float(del_x))*(u[0] - u[-2]) + (nu)*(del_t/float(np.power(del_x,2)))*(u[1] - 2*u[0] + u[-2])
        u_new[-1] = u_new[0]    # Defining the boundary conditions at x = 0 and x = L
    u = u_new.copy()            # Assigning the u for next iteration into current iteration for the next time step

plt.plot(x, u_new)
plt.show()
