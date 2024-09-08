def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Test
print(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))
<jupyter_output>
True
<jupyter_text>
Problem 2: Compute the area of a rectangle.
<jupyter_code>
