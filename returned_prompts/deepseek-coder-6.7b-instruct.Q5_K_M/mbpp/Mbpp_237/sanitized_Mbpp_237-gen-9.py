def check_occurences(lst):
    dic = {}
    for tup in lst:
        dic[tup] = dic.get(tup, 0) + 1
    return dic