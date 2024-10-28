def test_duplicate(test_tup):
    return len(test_tup) != len(set(test_tup))