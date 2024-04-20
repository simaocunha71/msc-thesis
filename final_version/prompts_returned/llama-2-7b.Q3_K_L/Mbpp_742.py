"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""

def area_tetrahedron(n):
    if (n>=4):
        return 0.1/6*(sum(i*i for i in range(n))-1)
    else:
        return -1
