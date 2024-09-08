def Find_Max(lst):
    max_len = -1
    max_element = []
    for element in lst:
        if len(element) > max_len:
            max_len = len(element)
            max_element = element
    return max_element

assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']


