def recursive_list_sum(test_list):
    total = 0
    for item in test_list:
        if type(item) == list:
            total += recursive_list_sum(item)
        else:
            total += item
    return total