def find_sum(my_list):
    return sum([x for i, x in enumerate(my_list) if x not in my_list[:i]])