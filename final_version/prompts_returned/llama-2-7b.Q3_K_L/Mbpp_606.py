"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(x):
    return x*math.pi/180 # x*pi/180 is the factor that we need to write
    
print("Result:",radian_degree(90))