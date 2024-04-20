"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""
import math
def find(a,b):
    print "find, ", a, b
    if(math.isnan(abs(float(a)/abs(float(b))))):
        return float("inf")
    else:
        print "The quotient is:"
        print (str((a/b)),end="\n")
        return (a/b)
#assert find(10,3) == 3
print find(2,98)