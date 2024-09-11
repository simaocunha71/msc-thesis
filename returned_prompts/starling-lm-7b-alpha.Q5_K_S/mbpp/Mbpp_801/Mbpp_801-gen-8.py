"""
def test_three_equal(a,b,c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 1
"""

def three_equal(a,b,c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 1

def test_three_equal(a,b,c):
    assert three_equal(1,1,1) == 3
    assert three_equal(2,2,2) == 3
    assert three_equal(3,3,3) == 3
    assert three_equal(1,1,2) == 2
    assert three_equal(1,1,3) == 2
    assert three_equal(1,2,3) == 2
    assert three_equal(1,3,2) == 2
    assert three_equal(2,3,1) == 2
    assert three_equal(2,1,3) == 2
    assert three_equal(3,2,1) == 2
    assert three_equal(3,1,2) == 2
    assert three_equal(2,3,2) == 2
    assert three_equal(2,2,3) == 2
    assert three_equal(3,2,3) == 2
    assert three_equal(3,3,2) == 2
    assert three_equal(1,2,2) == 2
    assert three_equal(1,1,3) == 2
    assert three_equal(1,3,1) == 2
    assert three_equal(2,1,1) == 2
    assert three_equal(2,3,1) == 2
    assert three_equal(3,1,1) == 2
    assert three_equal(3,2,1) == 2
    assert three_equal(3,1,2) == 2
    assert three_equal(2,