def test_three_equal(a,b,c):
    if a == b == c:
        return 3
    if a == b:
        if b == c:
            return 3
        elif a == c:
            return 3
    if b == c:
        if a == b:
            return 3
        elif a == c:
            return 3
    return 0