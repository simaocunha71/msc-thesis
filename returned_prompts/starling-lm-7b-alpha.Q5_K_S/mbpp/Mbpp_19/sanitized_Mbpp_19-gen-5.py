def test_duplicate(array):
    s = set(array)
    return len(s) != len(array)