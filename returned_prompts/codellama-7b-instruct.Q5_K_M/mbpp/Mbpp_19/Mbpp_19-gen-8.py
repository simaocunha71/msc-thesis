def test_duplicate(my_list):
    return len(my_list) != len(set(my_list))
