#!/usr/bin/python2.6

f = open("./evil2.gfx").read()

for i in range(5):
    open("lv12_%d.jpg" % i, "w").write(f[i::5])
