
def test_three_equal(a, b, c):
    return len([x for x in (a, b, c) if x == a])


