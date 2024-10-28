def count_X(my_tuple, element):
    count = 0
    for item in my_tuple:
        if item == element:
            count += 1
    return count