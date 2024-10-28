def merge_dictionaries_three(dic1,dic2,dic3):
    res = {}
    for i in dic1:
        res[i] = dic1[i]
    for i in dic2:
        res[i] = dic2[i]
    for i in dic3:
        res[i] = dic3[i]
    return res