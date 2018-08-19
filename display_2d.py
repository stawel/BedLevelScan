#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LightSource, BoundaryNorm
import numpy as np
import parse_points
import sys

file_name = "points.txt"
if len(sys.argv)>1: file_name = sys.argv[1]

X,Y,Z = parse_points.parse_file(file_name, Z_min=-0.8)

###### display 

fig = plt.figure()
ax = plt.subplot()

#surf = ax.contourf(X, Y, Z, cmap=cm.coolwarm, rstride=1, cstride=1)
surf = ax.pcolormesh( Z, cmap=cm.coolwarm)

fig.colorbar(surf)

numrows, numcols = Z.shape

def format_coord(x, y):
    x = int(x)
    y = int(y)
    if x >= 0 and x < numcols and y >= 0 and y < numrows:
        z = Z[y, x]
        return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
    else:
        return 'x=%1.4f, y=%1.4f' % (x, y)

ax.format_coord = format_coord

plt.show()

