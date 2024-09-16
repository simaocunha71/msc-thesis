def check_occurences(my_list):
    dict_occurences = {}
    for i in range(len(my_list)):
        if my_list[i] in dict_occurences:
            dict_occurences[my_list[i]] += 1
        else:
            dict_occurences[my_list[i]] = 1
    return dict_occurences