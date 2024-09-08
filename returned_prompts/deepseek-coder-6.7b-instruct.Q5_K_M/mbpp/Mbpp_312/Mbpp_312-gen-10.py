def volume_cone(radius, height):
    return (1./3) * math.pi * radius**2 * height

# Testing the function
print(math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001))

# Output: True
<jupyter_output>
True
<jupyter_text>
Exercise 2: Function to calculate the surface area of a cone.
<jupyter_code>
