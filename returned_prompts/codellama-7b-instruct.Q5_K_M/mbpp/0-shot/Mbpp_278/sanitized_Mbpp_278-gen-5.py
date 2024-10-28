def count_first_elements(my_tuple):
    count = 0
    for element in my_tuple:
        if type(element) == tuple:
            break
        count += 1
    return count