def check_occurences(lst):
    dic = {}
    for tup in lst:
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic