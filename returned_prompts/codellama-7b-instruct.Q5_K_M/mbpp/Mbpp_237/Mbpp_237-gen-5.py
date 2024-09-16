def check_occurences(list_of_tuples):
    occurences = {}
    for tup in list_of_tuples:
        if tup not in occurences:
            occurences[tup] = 0
        occurences[tup] += 1
    return occurences


