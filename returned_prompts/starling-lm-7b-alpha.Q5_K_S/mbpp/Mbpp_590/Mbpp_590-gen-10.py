"""
def polar_rect(r,theta):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return (x,y)

def test_polar_rect():
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    print("All tests passed.")

test_polar_rect()
"""

import math
def polar_rect(r,theta):
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    return (x,y)

def test_polar_rect():
    assert polar_rect(3,math.pi/2)==(0+0j,-3)
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    print("All tests passed.")

test_polar_rect()



"""
def polar_rect(r,theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return (x,y)
"""

"""
def test_polar_rect():
    assert polar_rect(3,math.pi/2)==(0+0j,-3)
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    print("All tests passed.")

test_polar_rect()
"""

"""
def polar_rect(r,theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x,y)
"""