def check_occurences(my_list):
    return {i: my_list.count(i) for i in set(my_list)}