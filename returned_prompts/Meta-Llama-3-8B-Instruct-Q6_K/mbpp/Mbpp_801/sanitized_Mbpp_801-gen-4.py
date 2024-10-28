def test_three_equal(a, b, c):
    count = 0
    if a == b and a == c:
        count = 3
    elif a == b:
        count = 2
    elif a == c:
        count = 2
    elif b == c:
        count = 2
    return count