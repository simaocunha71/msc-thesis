def check_occurences(lst):
    dictionary = {}
    for tup in lst:
        if tup in dictionary:
            dictionary[tup] += 1
        else:
            dictionary[tup] = 1
    return dictionary