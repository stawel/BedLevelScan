#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LightSource
import numpy as np
from sets import Set

file_name="points.txt"
values = 0                      # may be 0 or 1 (1 - is more accurate)
Z_min = [-0.7,-1000.]

##### read data from file
with open(file_name) as f:
    lines = f.readlines()

data = [ l.strip().split("Count")[values] for l in lines]

def parse(s):
    s1 = s.split(' ');
    x = y = z = 0.
    for vs in s1:
        v = vs.split(":")
        if v[0] == "X": x = float(v[1])
        if v[0] == "Y": y = float(v[1])
        if v[0] == "Z": z = float(v[1])
    return x,y,z


Zdict = dict()
Xset = Set()
Yset = Set()
for d in data:
    x,y,z = parse(d)
    if z < Z_min[values]: z = Z_min[values]
    Zdict[(x,y)] = z
    Xset.add(x)
    Yset.add(y)


#### generate matplotlib data

# Make data.
X = np.array(sorted(Xset))
Y = np.array(sorted(Yset))


#print "X:",X
#print "Y:",Y

Xp, Yp = np.meshgrid(X, Y)
Zp = np.zeros((len(Y),len(X)))
for i in range(len(X)):
    for j in range(len(Y)):
        Zp[j,i] = Zdict[(X[i],Y[j])]

#print "Xp:",Xp
#print "Yp:",Yp
#print "Zp:",Zp



###### display 
fig = plt.figure()
ax = fig.gca(projection='3d')


surf = ax.plot_surface(Xp, Yp, Zp, cmap=cm.coolwarm, rstride=1, cstride=1)

# Customize the z axis.
#ax.set_zlim(-2.00, 0.00)

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

