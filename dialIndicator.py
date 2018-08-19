#!/usr/bin/python
import serial
import time

port = "/dev/ttyS0"
baudrate = 115200
ser = serial.Serial(port, baudrate, timeout=1)



def read_old():
    while ser.inWaiting() > 5:
        ser.readline()

def get_value():
    s = ser.readline().split(" ")
    #print s
    if len(s)>2:
        return float(s[2])
    else:
        return -99999.


def get_position():
    read_old()
    return get_value()


def get_stable_position():
    read_old()
    x = -99999.
    get_value()
    y = get_value()
    while abs(x-y)>0.01:
        x = y
        get_value()
        y = get_value()
    return y



if __name__ == "__main__":
    while True:
        print "position: ", get_stable_position();

