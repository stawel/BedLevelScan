#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LightSource
import numpy as np
import parse_points

file_name = "points.txt"

X,Y,Z = parse_points.parse_file(file_name, Z_min=-0.7)

###### display 

fig = plt.figure()
ax = fig.gca(projection='3d')


surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=1, cstride=1)

# Customize the z axis.
#ax.set_zlim(-2.00, 0.00)

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

