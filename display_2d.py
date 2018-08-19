#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LightSource, BoundaryNorm
import numpy as np
import parse_points

file_name = "points.txt"

X,Y,Z = parse_points.parse_file(file_name, Z_min=-0.8)

###### display 

fig = plt.figure()
ax = plt.subplot()

#surf = ax.contourf(X, Y, Z, cmap=cm.coolwarm, rstride=1, cstride=1)
surf = ax.pcolormesh( Z, cmap=cm.coolwarm)

fig.colorbar(surf)

plt.show()

