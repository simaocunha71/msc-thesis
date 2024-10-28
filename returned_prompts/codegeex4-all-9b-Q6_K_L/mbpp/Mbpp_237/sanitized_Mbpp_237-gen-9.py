def check_occurences(lst):
    dict_occurences = {}
    for tup in lst:
        if tup in dict_occurences:
            dict_occurences[tup] += 1
        else:
            dict_occurences[tup] = 1
    return dict_occurences