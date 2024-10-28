def find_sum(my_list):
    return sum([i for i in set(my_list) if my_list.count(i) == 1])