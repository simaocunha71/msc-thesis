def check_occurences(lst):
    occurences = {}
    for item in lst:
        if item in occurences:
            occurences[item] += 1
        else:
            occurences[item] = 1
    return occurences