"""
def Find_Max(L):
    max_length = len(L[0])
    max_element = L[0]
    for i in range(len(L)):
        if len(L[i]) > max_length:
            max_length = len(L[i])
            max_element = L[i]
    return max_element
"""

def Find_Max(L):
    max_length = 0
    max_element = L[0]
    for i in range(len(L)):
        if len(L[i]) > max_length:
            max_length = len(L[i])
            max_element = L[i]
    return max_element

# print(Find_Max([['A'],['A','B'],['A','B','C']]))
# print(Find_Max([['A','B'],['C','D']]))
print(Find_Max(['A','B','C','D']))

# assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
# assert Find_Max([['A','B'],['C','D']]) == ['C','D']
# assert Find_Max(['A','B','C','D']) == ['A','B','C','D']
# assert Find_Max([['E','F','G'],['H','I','J']]) == ['E','F','G']
# assert Find_Max([['X','Y','Z'],['A','B','C']]) == ['X','Y','Z']
# assert Find_Max([['A'],['A','B'],['A','B','C'],['A','B','C','D']]) == ['A','B','C','D']
# assert Find_Max([]) == None
# assert Find_Max([None]) == None
# assert Find_Max([['A'],['A',None],['A','B']]) == ['A','B']
# assert Find_Max([['A'],['A',None],['A',None,'B']]) == ['A',None,'B']
# assert Find_Max([['A'],['A',None],['A',None,'B'],['A',