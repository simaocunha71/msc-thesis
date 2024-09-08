def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

# test case
print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

# True means the function is correct
<jupyter_output>
True
<jupyter_text>
Problem 3
<jupyter_code>
