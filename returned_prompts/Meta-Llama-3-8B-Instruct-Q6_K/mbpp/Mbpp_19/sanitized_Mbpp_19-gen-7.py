def test_duplicate(lst):
    return len(lst) != len(set(lst)) # if the length of the list is not equal to the length of the set of the list, it means there are duplicates in the list. 