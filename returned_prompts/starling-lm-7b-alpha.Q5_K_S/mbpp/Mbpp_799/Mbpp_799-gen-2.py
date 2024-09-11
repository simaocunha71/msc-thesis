"""
def left_rotate(n, d):
    d = d % 32
    return (n << d) | (n >> (32 - d))

"""
def left_rotate(n, d):
    return (n << d) | (n >> (32 - d))

def test_left_rotate():
    assert left_rotate(16, 2) == 64
    print("All tests passed")

test_left_rotate()

"""

