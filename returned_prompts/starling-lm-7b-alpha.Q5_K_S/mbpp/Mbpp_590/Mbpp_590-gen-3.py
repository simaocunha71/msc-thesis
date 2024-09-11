"""
def polar_rect(r, theta):
    return (r*np.cos(theta), r*np.sin(theta))

def test_polar_rect():
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    print('All tests passed.')

if __name__ == '__main__':
    test_polar_rect()
"""

from math import sin, cos, pi

def polar_rect(r, theta):
    return (r * cos(theta), r * sin(theta))

def test_polar_rect():
    assert polar_rect(3, 4) == (5, 0.9272952180016122 + 0j, -2 + 2.4492935982947064e-16j)
    print('All tests passed.')

if __name__ == '__main__':
    test_polar_rect()



"""
As you can see, the rectangular coordinates of (3, 4) in polar coordinates are (r, θ) = (5, 0.9272952180016122).
In the rectangular coordinate system, the point (5, 0.9272952180016122) lies on the x-axis, while the point (-2 + 2.4492935982947064e-16j) lies on the y-axis.
"""

# Convert polar coordinates to rectangular coordinates
def polar_rect(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)

# Test the function
def test_polar_rect():
    assert polar_rect(3, 4) == (5, 0.927295218