def test_three_equal(a, b, c):
    return sum([1 for x in [a,b,c] if x == a])