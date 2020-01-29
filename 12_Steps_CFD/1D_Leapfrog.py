import numpy as np
import matplotlib.pyplot as plt

x_max = 4
x_points = 51
t_points = 100
del_x = 0.1
c = 1
del_t = 0.001

x = np.linspace(0, x_max, x_points)
u = np.zeros(x_points)
for i in range(0, x_points):
    if x[i] > 0 and x[i] < 2:
        u[i] = 1


u_new = np.zeros(x_points)
u_old = np.zeros(x_points)

for it in range(0, t_points):
    for ix in range(1, x_points-1):
        u_new[ix] = u_old[ix-1] - (c*del_t/float(del_x))*(u[ix+1] - u[ix-1])

    u_old = u.copy()
    u = u_new.copy()


plt.plot(x,u)
plt.show()