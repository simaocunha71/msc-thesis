
def lateralsurface_cylinder(radius, height):
    return 2 * math.pi * radius * height

#Testing the function
print(math.isclose(lateralsurface_cylinder(10,5), 314.15000000000003, rel_tol=0.001))

#Result: True
#So, the function is correct.

#Testing the function with different inputs
print(lateralsurface_cylinder(3,6))
print(lateralsurface_cylinder(5,7))

#Results:
# 37.69911184307752
# 106.44025842096778
<jupyter_output>
True
37.69911184307752
106.44025842096778
<jupyter_text>
Question 4:Given the coordinates of a center of a circle, its start angle and its end angle, write a function to calculate the area of a sector.
<jupyter_code>
