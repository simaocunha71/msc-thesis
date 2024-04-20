"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""
import math

def parabola_directrix(a,b,c):
    '''
      The parabola y = ax + bx^2 has its directrix the circle x^2+ax+b=0.
       Note that a and b are real numbers.  If you take them to be negative
        integers, then this formula does not make sense.
    '''
    return (-c/(b*2))**(1/2)