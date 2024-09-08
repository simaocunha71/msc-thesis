def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

# Test case
print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

# True means the function is working correctly
# False means the function is not working correctly
<jupyter_output>
True
<jupyter_text>
Task 2:Write a function called `perimeter_square` that takes one argument `side_length` and returns the perimeter of a square.The formula for the perimeter of a square is `4*side_length`.
<jupyter_code>
# Solution:
def perimeter_square(side_length):
    return 4 * side_length
<jupyter_output>
<empty_output>
<jupyter_text>
Task 3:Write a function called `volume_cylinder` that takes two arguments `radius` and `height` and returns the volume of a cylinder.The formula for the volume of a cylinder is `π*radius^2*height`.
<jupyter_code>
# Solution:
def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height
<jupyter_output>
<empty_output>
<jupyter_text>
Task 4:Write a function called `surfacearea_cylinder` that takes two arguments `radius` and `height` and returns the surface area of a cylinder.The formula for the surface area of a cylinder is `2*π*radius*(radius+height)`.
<jupyter_code>
# Solution:
def surfacearea_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)
<jupyter_output>
<empty_output>
<jupyter_text>
Task 5:Write a function called `circumference_circle` that takes one argument `radius` and returns the circumference of a circle.The formula for the circumference of