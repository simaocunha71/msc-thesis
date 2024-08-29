def volume_cylinder(radius, height):
    return 3.14159 * radius**2 * height

print(volume_cylinder(10,5))
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
<jupyter_output>
1570.7963267948966
<jupyter_text>
Problem 3:
<jupyter_code>
