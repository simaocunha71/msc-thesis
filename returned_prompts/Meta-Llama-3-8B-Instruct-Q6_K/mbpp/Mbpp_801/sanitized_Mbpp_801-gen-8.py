def test_three_equal(a, b, c):
    return a == b == c and 3 or a == b and 2 or a == c and 2 or b == c and 2 or 0