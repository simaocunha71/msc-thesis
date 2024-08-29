def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

# testing the function
print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

# Output:
# True
<jupyter_output>
True
<jupyter_text>
Exercise 1.2: Volume of a Sphere The volume of a sphere is given by the formula $\frac{4}{3} \times \pi \times r^3$. Implement this formula in a function called `volume_sphere`.
<jupyter_code>
