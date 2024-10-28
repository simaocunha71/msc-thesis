def test_duplicate(lst):
    return len(lst) != len(set(lst))  # True if the list contains duplicate elements, False otherwise.