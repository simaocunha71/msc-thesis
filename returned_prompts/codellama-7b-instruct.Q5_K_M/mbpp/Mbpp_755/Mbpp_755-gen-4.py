def second_smallest(my_list):
    smallest = min(my_list)
    return min(x for x in my_list if x != smallest)
