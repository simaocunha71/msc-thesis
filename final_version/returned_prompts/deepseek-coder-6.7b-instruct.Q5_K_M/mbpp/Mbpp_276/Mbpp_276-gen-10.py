def volume_cylinder(radius, height):
    return math.pi * radius**2 * height

print(volume_cylinder(10,5))

# The function volume_cylinder calculates the volume of a cylinder using the formula:
# Volume = πr²h
# where r is the radius of the cylinder and h is the height.

# The function math.isclose() is used to compare the result of the function with the expected result. The parameter rel_tol is used to set the relative tolerance for the comparison. If the result is within the relative tolerance, the function returns True. Otherwise, it returns False.

# The expected result is 1570.7500000000002, so the relative tolerance is set to 0.001. If the result of the function volume_cylinder(10,5) is within 0.001 of 1570.7500000000002, the function math.isclose() returns True. Otherwise, it returns False.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
<jupyter_output>
1570.7963267948966
<jupyter_text>
Task 7
<jupyter_code>
