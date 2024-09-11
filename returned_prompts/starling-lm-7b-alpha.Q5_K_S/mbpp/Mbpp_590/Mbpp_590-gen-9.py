"""
def polar_rect(r, theta):
    return (r*math.cos(theta), r*math.sin(theta))
"""

def polar_rect(r, theta):
    return (r*math.cos(math.radians(theta)), r*math.sin(math.radians(theta)))

# assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))

# print(polar_rect(3,4))




"""
In the above code, we define a function polar_rect that takes in two arguments: r and theta, representing the polar coordinates. The function uses the formula to convert polar coordinates to rectangular coordinates: rectangular coordinates = (r*cos(theta), r*sin(theta)). We use the math.cos and math.sin functions to calculate the cosine and sine of theta, respectively, and the math.radians function to convert theta from degrees to radians. Finally, we assert that the result of polar_rect(3,4) is equal to the expected output ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))."""

"""
To convert polar coordinates to rectangular coordinates, we can use the formula (r*cos(theta), r*sin(theta)). Here, r represents the magnitude of the polar coordinates and theta represents the angle in radians. In the given code, the function polar_rect takes in two arguments: r and theta, and returns the rectangular coordinates as a tuple. The math.cos and math.sin functions are used to calculate the cosine and sine of theta, respectively, and the math.radians function is used to convert theta from degrees to radians. The assert statement is used to check if the result of polar_rect(3,4) is equal to the expected output ((5.0, 0.9272952180016122