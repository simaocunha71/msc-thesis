"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""
from math import sin, cos
def radian_degree(x):
    "Returns the value of x in both degrees and radians."
    
    if type(x) != float:
        raise TypeError("argument is not a number")
    return (cos(x))/180. - 2 * sin((x+90)/2.)/(180./2.), cos((x+90)/2.)/180. + sin(x) #(sin(x)*sin(90))+(cos(x))
    
def degee_radian(x):
    "Returns the value of x in both degrees and radians."
    
    if type(x) != float:
        raise TypeError("argument is not a number")