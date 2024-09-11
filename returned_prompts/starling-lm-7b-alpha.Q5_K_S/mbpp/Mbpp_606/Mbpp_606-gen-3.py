"""
def radian_degree(degrees):
    return degrees*math.pi/180
"""

def radian_degree(degrees):
    return degrees*math.pi/180

# assert radian_degree(90)==1.5707963267948966




"""
Write a function to convert radians to degrees.
assert radian_degree(1.5707963267948966)==90
"""

def degree_radian(radians):
    return radians*180/math.pi

# assert degree_radian(1.5707963267948966)==90





"""
Write a function to convert degrees to centigrade.
assert fahrenheit_celsius(32)==0
"""
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

# assert fahrenheit_celsius(32)==0

"""
Write a function to convert centigrade to Fahrenheit.
assert celsius_fahrenheit(0)==32
"""
def celsius_fahrenheit(celsius):
    return celsius*9/5+32

# assert celsius_fahrenheit(0)==32

"""
Write a function to convert kilometers to miles.
assert kilometers_miles(0.621371)==0.372822128
"""
def kilometers_miles(kilometers):
    return kilometers*0.621371

# assert kilometers_miles(0.621371)==0.372822128

"""
Write a function to convert miles to kilometers.
assert miles_kilometers(0.372822128)==0.621371
"""
def miles_kilometers(miles):
    return miles/0.621371