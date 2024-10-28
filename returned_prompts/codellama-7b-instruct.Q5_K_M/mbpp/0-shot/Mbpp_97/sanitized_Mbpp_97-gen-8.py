def frequency_lists(lst):
    dic = {}
    for sublist in lst:
        for item in sublist:
            dic[item] = dic.get(item, 0) + 1
    return dic