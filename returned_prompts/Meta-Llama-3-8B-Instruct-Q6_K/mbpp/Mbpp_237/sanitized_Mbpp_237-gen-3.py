def check_occurences(tuples_list):
    return {tuple(sorted(t)): tuples_list.count(t) for t in set(tuple(sorted(t)) for t in tuples_list)}