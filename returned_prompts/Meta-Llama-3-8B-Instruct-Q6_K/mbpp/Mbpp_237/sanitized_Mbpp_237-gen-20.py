def check_occurences(lst):
    result = {}
    for tuple in lst:
        if tuple in result:
            result[tuple] += 1
        else:
            result[tuple] = 1
    return result