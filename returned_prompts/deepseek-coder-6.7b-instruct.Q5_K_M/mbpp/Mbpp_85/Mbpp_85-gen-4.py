def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

"""
Explanation:
The formula to calculate the surface area of a sphere is 4 * pi * radius ** 2.
The function takes the radius of the sphere as an argument, calculates the surface area using the formula, and returns the result.
We use math.isclose() to compare the result with the expected value, which allows for a small tolerance for floating point errors.
"""
<jupyter_output>
True
<jupyter_text>
Exercise 2
<jupyter_code>
