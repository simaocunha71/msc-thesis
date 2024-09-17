def polar_rect(r, theta):
    import cmath
    rect_x = r * cmath.cos(theta)
    rect_y = r * cmath.sin(theta)
    return (rect_x, rect_y)  # or return complex(rect_x, rect_y) if you prefer a complex number output
    # the unit test provided is: assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)) which suggests the function should return a tuple of two complex numbers. So, we return a tuple of two values as requested in the problem description. 