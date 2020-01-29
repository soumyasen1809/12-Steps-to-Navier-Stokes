import numpy as np
from matplotlib import pyplot as plt

x_max = 2     # Domain length in X
x_points = 101   # Number of grid points in X
t_points = 50   # Number of time steps
nu = 0.3        # Viscosity
del_x = x_max/float(x_points - 1)   # Delta x (grid length)
del_t = 0.2*np.power(del_x,2)/nu    # Delta t (time interval)

x = np.linspace(0,x_max,x_points)
u = np.ones(x_points)
u[0] = 0
u[x_points - 1] = 0
# Defining boundary conditions
for i in range(0, x_points):
    if x[i] >= 0.5 and x[i] <= 1.0 :
        u[i] = 2.0

# Solve the linear 1D equation
u_new = np.ones(x_points)

for it in range(0, t_points):
    for ix in range(2, x_points-1):
        u_new[ix] = u[ix] + (nu)*(del_t/float(np.power(del_x,2)))*(u[ix+1] - 2*u[ix] + u[ix-1])
    u = u_new.copy()

plt.plot(x, u_new)
plt.show()