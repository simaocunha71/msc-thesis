"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""

def lateral_surface_area_cylinder(r1,r2):
    return (math.pi * r2**2 - math.pi*(r1 + r2) ** 2)/4
