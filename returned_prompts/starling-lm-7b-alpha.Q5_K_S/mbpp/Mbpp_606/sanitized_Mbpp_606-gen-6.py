from math import pi
from hypothesis import given, settings, assume, reproduce
from hypothesis.strategies import floats
from hypothesis import given, settings, assume, reproduce
from hypothesis.strategies import floats
def radian_degree(x):
    return x*(2*3.14159265358979323846/360)