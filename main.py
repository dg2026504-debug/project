Web VPython 3.2
import random
sphere(pos = vec(0,0,0), color = color.white, radius = 1)
sphere(pos = vec(0.8,0.8,0), color = color.white, radius = 0.3)
sphere(pos = vec(-0.8,0.8,0), color = color.white, radius = 0.3)
sphere(pos = vec(0,0.4,1), color = color.black, radius = 0.05)
cylinder(axis = vec(0,0,1), pos = vec(0,0.1,1), color = color.red, radius = 0.2, length = 0.05)
x = sphere(pos = vec(0.3,0.5,0.8), color = vec(random.random(),random.random(),random.random()), radius = 0.07)
y = sphere(pos = vec(-0.3,0.5,0.8), color = vec(random.random(),random.random(),random.random()), radius = 0.07)

while True : 
    rate(100)
    x.color = vec(random.random(),random.random(),random.random())
    y.color = vec(random.random(),random.random(),random.random())
