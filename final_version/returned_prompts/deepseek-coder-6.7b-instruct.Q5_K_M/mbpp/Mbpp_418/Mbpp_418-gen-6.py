
def Find_Max(list_val):
    max_len = -1
    max_list = []
    for l in list_val:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return max_list

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""


def Find_Max(list_val):
    return max(list_val, key=len)

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

"""
