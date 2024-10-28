import math

def surfacearea_sphere(radius):
    pi = math.pi
    return 4 * pi * radius ** 2 + 2 * pi * radius * math.sqrt(radius ** 2)


