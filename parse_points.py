#!/usr/bin/python

import numpy as np
from sets import Set


def generate_matplotlib_data(Xset, Yset, Zdict):
    # Make data.
    X = np.array(Xset)
    Y = np.array(Yset)

    Xp, Yp = np.meshgrid(X, Y)
    Zp = np.zeros((len(Y),len(X)))
    for i in range(len(X)):
        for j in range(len(Y)):
            Zp[j,i] = Zdict[(X[i],Y[j])]

    #print "Xp:",Xp
    #print "Yp:",Yp
    #print "Zp:",Zp
    return Xp, Yp, Zp


def parse_xyz(s):
    s1 = s.split(' ');
    x = y = z = 0.
    for vs in s1:
        v = vs.split(":")
        if v[0] == "X": x = float(v[1])
        if v[0] == "Y": y = float(v[1])
        if v[0] == "Z": z = float(v[1])
    return x,y,z


def parse_file(file_name, Z_min = None, values = 0):

    with open(file_name) as f:
        lines = f.readlines()

    data = [ l.strip().split("Count")[values] for l in lines]

    Zdict = dict()
    Xset = Set()
    Yset = Set()
    for d in data:
        x,y,z = parse_xyz(d)
        if Z_min is not None and z < Z_min: z = Z_min
        Zdict[(x,y)] = z
        Xset.add(x)
        Yset.add(y)

    return generate_matplotlib_data(sorted(Xset), sorted(Yset), Zdict)


