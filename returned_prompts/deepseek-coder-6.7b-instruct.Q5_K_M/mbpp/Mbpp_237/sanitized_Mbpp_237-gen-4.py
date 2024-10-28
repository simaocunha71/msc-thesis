def check_occurences(lst):
    result = {}
    for tup in lst:
        if tup in result:
            result[tup] += 1
        else:
            result[tup] = 1
    return result