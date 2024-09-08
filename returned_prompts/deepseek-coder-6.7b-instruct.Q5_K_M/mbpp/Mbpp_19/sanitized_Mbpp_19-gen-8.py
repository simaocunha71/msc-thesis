def test_duplicate(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True