def surfacearea_sphere(radius):
    return 4 * 3.14159 * radius ** 2

print(surfacearea_sphere(10))

assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

#Problem 3

