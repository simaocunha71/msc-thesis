"""
def volume_sphere(radius):
    return (4/3) * math.pi * radius**3
"""

# ------------------------
# Code
# ------------------------

# ------------------------
# Code
# ------------------------
def volume_sphere(radius):
    return (4/3) * math.pi * radius**3

# ------------------------
# Test Cases
# ------------------------
print(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

# ------------------------
# Test Cases
# ------------------------
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

# ------------------------
# Test Cases
# ------------------------
print(volume_sphere(10))

# ------------------------
# Test Cases
# ------------------------
assert volume_sphere(10) == 4188.790204786391
<jupyter_output>
True
4188.790204786391
True
<jupyter_text>
Problem 2:Create a function to calculate the area of a square. The function should take one argument, side_length, and return the area.assert math.isclose(area_square(10), 100, rel_tol=0.001)
<jupyter_code>
# ------------------------
# Code
# ------------------------
def area_square(side_length):
    return side_length ** 2

# ------------------------
# Test Cases
# ------------------------
assert math.isclose(area_square(10), 100, rel_tol=0.001)
print(area_square(10))
<jupyter_output>
100
<jupyter_text>
Problem 3:Create a function that calculates the hypoten