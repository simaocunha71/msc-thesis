def Find_Max(lst):
    max_len = -1
    max_ele = []
    for ele in lst:
        if len(ele) > max_len:
            max_len = len(ele)
            max_ele = ele
    return max_ele

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']


