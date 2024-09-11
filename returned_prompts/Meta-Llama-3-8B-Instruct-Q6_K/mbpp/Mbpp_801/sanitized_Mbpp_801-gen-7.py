def test_three_equal(a, b, c):
    if a == b == c:
        return 3
    else:
        return 0
    #or return sum([a, b, c]) if a == b == c else 0