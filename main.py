Web VPython 3.2
import random
z_face = sphere(pos = vec(0,0,0), color = color.white, radius = 1)
z_ear1 = sphere(pos = vec(0.8,0.8,0), color = color.white, radius = 0.3)
z_ear2 = sphere(pos = vec(-0.8,0.8,0), color = color.white, radius = 0.3)
z_nose = sphere(pos = vec(0,0.4,1), color = color.black, radius = 0.05)
z_mouth = cylinder(axis = vec(0,0,1), pos = vec(0,0.1,1), color = color.red, radius = 0.2, length = 0.05)
z_eye1 = sphere(pos = vec(0.3,0.5,0.8), color = color.black, radius = 0.07)
z_eye2 = sphere(pos = vec(-0.3,0.5,0.8), color = color.black, radius = 0.07)

z = compound([z_face,z_ear1,z_ear2,z_nose,z_mouth,z_eye1,z_eye2])
while True : 
    rate(50)
    k = keysdown()
    if ' ' in k:
        z.pos.x = random.uniform(-5,5)
        z.pos.y = random.uniform(-5,5)
