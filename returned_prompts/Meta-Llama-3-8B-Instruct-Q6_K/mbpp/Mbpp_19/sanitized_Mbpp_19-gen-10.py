def test_duplicate(lst):
    return len(lst) != len(set(lst)) # returns True if there are duplicate elements, False otherwise