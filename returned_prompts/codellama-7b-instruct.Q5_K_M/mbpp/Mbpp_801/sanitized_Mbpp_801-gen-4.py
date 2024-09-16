def test_three_equal(a, b, c):
    if a == b == c:
        return 3
    count = 0
    if a == b:
        count += 1
    if b == c:
        count += 1
    if a == c:
        count += 1
    return count