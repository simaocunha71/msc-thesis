def max_aggregate(tuples_list):
    dict_aggregate = {}
    for student, score in tuples_list:
        if student in dict_aggregate:
            dict_aggregate[student] += score
        else:
            dict_aggregate[student] = score
    return max(dict_aggregate.items(), key=lambda x: x[1])