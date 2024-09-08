def Find_Max(list_elements):
    return max(list_elements, key=len)

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']


