
def check_occurences(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))



"""
