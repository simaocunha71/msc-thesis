def check_occurences(tuples_list):
    occurrence_dict = {}
    for t in tuples_list:
        if t in occurrence_dict:
            occurrence_dict[t] += 1
        else:
            occurrence_dict[t] = 1
    return occurrence_dict