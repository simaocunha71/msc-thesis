def find_sum(my_list):
    return sum([x for x in my_list if my_list.count(x) == 1])