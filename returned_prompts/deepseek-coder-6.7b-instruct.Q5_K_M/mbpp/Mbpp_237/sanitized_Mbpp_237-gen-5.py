def check_occurences(tup_list):
    dict_count = {}
    for tup in tup_list:
        if tup in dict_count:
            dict_count[tup] += 1
        else:
            dict_count[tup] = 1
    return dict_count