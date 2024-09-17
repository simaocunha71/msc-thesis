def count_X(test_tuple, element):
    count = 0
    for i in test_tuple:
        if i == element:
            count += 1
    return count