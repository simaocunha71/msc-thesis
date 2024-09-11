def check_occurences(tuples_list):
    tuple_dict = {}
    for i in tuples_list:
        if i in tuple_dict:
            tuple_dict[i] += 1
        else:
            tuple_dict[i] = 1
    return tuple_dict