def volume_sphere(radius):
    return (4/3)*math.pi*radius**3

print(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))


