def test_duplicate(array):
    set_array = set(array)
    if len(set_array) != len(array):
        return True
    else:
        return False