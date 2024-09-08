def volume_sphere(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# Testing the function
print(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

# Expected output: True
<jupyter_output>
True
<jupyter_text>
Exercise 2: Calculating the Surface Area of a Sphere
<jupyter_code>
