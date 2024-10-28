
def test_duplicate(test_tup):
    if len(test_tup) != len(set(test_tup)):
        return True
    else:
        return False


