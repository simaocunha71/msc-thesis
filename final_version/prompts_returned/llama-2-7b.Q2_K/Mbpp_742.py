"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
from math import sqrt, sin, cos, pi

def area_triangle(length):
    """Calculate the area of an isosceles triangle with base "b", and height "a".
    """
    return length * (sin(pi/3) - 0.25) / 180

class Tetrahedron:
    def __init__(self, a, b, c):
        self.points = [T(a), T(b), T(c)]
        
    def area(self):
        return sum([area_triangle(p[0]) for p in self.points])
    
class Vector:
    """Vector class"""
    def __init__(self, a=0, b=1, c=2):
        self.a = a
        self.b = b
        self.c = c
        
    def magnitude(self):
        return sqrt((self.a**2+self.b**2-self.c**2)/2)
    
    def normalize(self):
        return (self*magnitude())/magnitude()
    
    @staticmethod
    def cross(v1, v2):
        """Calculate the vector product of v1 and v2"""  # noqa: E501
        return Vector(
            v1.c + v2.a*(v1.b-v1.c) - (v1.a+v2.b-v2.c)*v1.c,
            v2.b + v1.d - (v1.b + v2.d - v2.c)*v2.d,
            v1.d + v2.c*(v1.a+v1.b-v1.c) - (v1.d+v2.a*(v1.b-v1.d)+v2.b-v2.c))
            
    @staticmethod
    def dot(v1, v2):
        """Dot product of two vectors"""  # noqa: E501
        return (v1.a*v2.a + v1.b*v2.b) - (v1.c*v2.d