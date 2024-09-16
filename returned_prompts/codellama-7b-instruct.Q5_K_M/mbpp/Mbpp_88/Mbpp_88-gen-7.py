def freq_count(my_list):
    return dict((x, my_list.count(x)) for x in set(my_list))
