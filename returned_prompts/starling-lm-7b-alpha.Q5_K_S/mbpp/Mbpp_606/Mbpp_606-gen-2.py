"""
def radian_degree(degree):
    return degree * (3.1415926535897932 / 180)

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966
    print('All tests passed.')

test_radian_degree()
"""

def radian_degree(degree):
    return degree * (3.1415926535897932 / 180)

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966
    print('All tests passed.')

test_radian_degree()




"""
Write a function to calculate the area of a circle with radius r. The radius should be in degrees.

assert circle_area(1) == 3.141592653589793

"""

def circle_area(r):
    r_radians = radian_degree(r)
    return 3.1415926535897932 * (r_radians ** 2)

def test_circle_area():
    assert circle_area(1) == 3.141592653589793
    print('All tests passed.')

test_circle_area()

"""
Write a function to calculate the circumference of a circle with radius r. The radius should be in degrees.

assert circle_circumference(1) == 3.141592653589793

"""
def circle_circumference(r):
    r_radians = radian_degree(r)
    return 3.1415926535897932 * 2 * r_radians

def test_circle_circumference():
    assert circle_circumference(1) == 3.1415926