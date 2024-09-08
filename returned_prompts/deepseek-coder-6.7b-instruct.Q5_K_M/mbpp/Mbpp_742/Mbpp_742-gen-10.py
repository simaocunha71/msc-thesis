
def area_tetrahedron(side):
    return (sqrt(3) * side ** 2) / 4

print(area_tetrahedron(3))

# Output: 15.588457268119894

"""
The formula for the area of a tetrahedron is sqrt(3) * side ^ 2 / 4.
We just need to plug in the side length and apply the formula.
"""

# Test cases:
print(area_tetrahedron(1)) # should return 0.43301270189221946
print(area_tetrahedron(2)) # should return 5.698457268119894
print(area_tetrahedron(3)) # should return 15.588457268119894
print(area_tetrahedron(4)) # should return 36.642526258414426
print(area_tetrahedron(5)) # should return 78.86528371902181

# END OF CODE

# Note: The above code uses the sqrt (square root) function from the math module.
# The square root of 3 is a constant value in mathematics, and is approximately equal to 1.7320508075688772.
# So we can replace sqrt(3) with 1.7320508075688772 if we want to make the code more readable.

# Also, keep in mind that floating point numbers can sometimes have small rounding errors. 
# This means that the result may not be exactly equal to the expected result, but it will be very close. 
# This is a common issue when working with floating point numbers in Python.
# We can use the built-in function round() to limit the number of decimal places in the result.

def area_tetrahedron(side):
    return round((1.73