def test_three_equal(a, b, c):
    count = 0
    if a == b == c:
        count = 3
    elif a == b or b == c or a == c:
        count = 2
    return count