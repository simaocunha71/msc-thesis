def test_three_equal(a, b, c):
    return int((a == b) + (a == c) + (b == c))