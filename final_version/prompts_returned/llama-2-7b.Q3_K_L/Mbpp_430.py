"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
from math import sqrt
def parabola_directrix(x,y,f): #function for finding the directrix
	return -sqrt((3*y-4*f)/(4*x+6))
#print (parabola_directrix(-2,-3,1), -198) 