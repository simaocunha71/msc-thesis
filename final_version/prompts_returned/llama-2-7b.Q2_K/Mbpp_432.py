"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
import math
def median_trapezium(a,b,c):
    if len(set(a))!=len(set([-999.-9])):
        return math.fabs(median_trapezium(float(a[1]), float(b), c) - median_trapezium(float(a[0])+1,float(c)-1, float(b)))
    else:
        return -9999
