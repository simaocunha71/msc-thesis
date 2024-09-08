def test_three_equal(a,b,c):
    count = 0
    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1
    return count