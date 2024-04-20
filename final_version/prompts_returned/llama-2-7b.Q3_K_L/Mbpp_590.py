"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""

def polar_rect(x, y):
    x = np.cos(np.pi * x)
    y = np.sin(np.pi * y)
    return (x.real, -y.real), (x.imag, y.imag)
