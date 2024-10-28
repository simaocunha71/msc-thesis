def check_smaller(first_tuple, second_tuple):
    return all(x < y for x, y in zip(first_tuple, second_tuple))