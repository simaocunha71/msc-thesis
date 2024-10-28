def recursive_list_sum(my_list):
    if type(my_list)==list:
        return sum([recursive_list_sum(i) for i in my_list])
    else:
        return my_list