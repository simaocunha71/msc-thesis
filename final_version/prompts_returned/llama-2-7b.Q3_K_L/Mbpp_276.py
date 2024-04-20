"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    return 360 * radius**2 * height
\end{code}

Comment: The `input` parameter should be a **tuple** of the two arguments you pass to the function. You can also use f-strings in this case and remove the assignment lines if you like; but it's not necessary for this particular problem.