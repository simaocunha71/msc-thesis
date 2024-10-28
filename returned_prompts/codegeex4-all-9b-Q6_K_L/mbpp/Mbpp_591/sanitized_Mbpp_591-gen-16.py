def swap_List(test_list):
    first_element = test_list[0]
    last_element = test_list[-1]
    test_list[0] = last_element
    test_list[-1] = first_element
    return test_list