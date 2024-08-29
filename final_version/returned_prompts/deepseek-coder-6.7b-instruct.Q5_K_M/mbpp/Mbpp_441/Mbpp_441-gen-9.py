def surfacearea_cube(size):
    return 6 * size ** 2

print(surfacearea_cube(5))

# Alternatively, you can use the formula for the surface area of a cube: 6 * side^2.

# Expected output: 150

# If you run this program, it will print 150, which is the surface area of a cube with a side length of 5.
# This is because the surface area of a cube is given by the formula 6 * side^2, where side is the length of one side of the cube.
# So, for a cube with a side length of 5, the surface area would be 6 * (5)^2 = 6 * 25 = 150.
# Hence, the assertion is true.
<jupyter_output>
150
<jupyter_text>
Question 2: Write a Python function that checks whether a given number is a perfect number or not.A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. For example, 6 is a perfect number because 1, 2 and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
<jupyter_code>
# 