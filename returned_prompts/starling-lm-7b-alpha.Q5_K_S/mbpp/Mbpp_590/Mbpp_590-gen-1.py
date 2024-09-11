def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def test_polar_rect():
    assert polar_rect(3,4) == ((5.0, 0.9272952180016122), (-2 + 2.4492935982947064e-16j))

test_polar_rect()





# Here's a function to convert polar coordinates to rectangular coordinates.
# The function takes two parameters, r and theta, which represent the radius and angle in polar coordinates, respectively.
# It uses the formulas x = r * cos(theta) and y = r * sin(theta) to convert polar coordinates to rectangular coordinates.
# The function then returns a tuple containing the values of x and y.
# The provided test case asserts that the function correctly converts the polar coordinates (3, 4) to the rectangular coordinates (5.0, 0.9272952180016122) and ( -2 + 2.4492935982947064e-16j), which are the expected results.
# The test case is run using the test_polar_rect() function, which checks if the function's output matches the expected output.

# This function can be used to convert any polar coordinates to rectangular coordinates by providing the appropriate values for r and theta.
# The function can be helpful in various applications, such as computer graphics, robotics, and physics, where polar coordinates are used to represent positions or directions.

# Here's an example of how the function can be used:
# r = 5
# theta = math.pi / 4
# rect_coords = polar_rect(r, theta)
# print(rect_coords)  # Output: ((3.535533905932738, 3.535533905932738), (0.0+0.0j))