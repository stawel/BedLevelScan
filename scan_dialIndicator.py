#!/usr/bin/python
import serial
import time
import dialIndicator

port = "/dev/ttyUSB0"
baudrate = 250000
ser = serial.Serial(port, baudrate, timeout=5)

X_max = 320             # X dimension in mm
X_min = 0
Y_max = 308             # Y dimension in mm
Y_min = 38
X_res = 100
Y_res = 100
G38_F = 1000            # G38 feedrate (probe)
G1_F = 6000             # G1 feedrate (move)
Z_max = 6.5             # Z maximum position
Z_min = 5               # Z minimum position

zigzag_order = True
output_file = "points.txt"


def send(s, comment = ''):
    ser.write(s+"\n")
    if comment != '':   print s, "\t# ", comment
    else:               print s

def read_init():
    r = ''
    s = False
    while r != 'ok':
        r = ser.readline().strip()
        if r == '' and not s:
            send("M400")
            s = True
        print r


def wait_for(w):
    r = ''
    result = []
    while r != w:
        r = ser.readline().strip()
        print r
        result.append(r)
        if r[0:5] == "Error": raise AssertionError("got an error: " + r)
    return result

def run(c, comment = ''):
    send(c, comment)
    return wait_for('ok')


def c_add(c, vs, v):
    if v is not None: c+= ' ' + vs + str(v)
    return c

def c_add_xyz(c, x, y, z, f):
    c = c_add(c, "F", f)
    c = c_add(c, "X", x)
    c = c_add(c, "Y", y)
    c = c_add(c, "Z", z)
    return c


def G1(x = None, y = None, z = None):
    run(c_add_xyz("G1", x, y, z, G1_F))

def d(s):
    print "DEBUG: ", s

def get_point(x,y):
    G1(x, y, Z_max)
    G1(x, y, Z_min)
    run("M400")
    z = dialIndicator.get_stable_position()
    G1(x, y, Z_max)
    return z

def main():
    out = open(output_file,"w")
    read_init()
    d("init command")
    run("G90", "Set to Absolute Positioning")
    run("G28", "Move to Origin (Home)")
    run("M211 S0",  "Disable Software Endstops")
    for j in range(0, Y_res):
        for i in range(0, X_res):
            if (j % 2) == 1 and zigzag_order:   ii = X_res-i-1
            else:                               ii = i
            x = X_min + (X_max-X_min) * ii/(X_res-1)
            y = Y_min + (Y_max-Y_min) *  j/(Y_res-1)
            z = get_point(x, y)
            o = "X:" + str(x) + " Y:" + str(y) + " Z:" +str(z) + "\n"
            print o
            out.write(o)

main()
