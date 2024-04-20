"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    """
       Returns the volume of a cylinder, given its radius and height as input
       
       Usage:
           >>> vol = volume_cylinder(5, 3.5)
           #outputs: 916.2374999999998
    """
     return (math.pi * radius**2)/3.0 + (radius*height)

#end of program