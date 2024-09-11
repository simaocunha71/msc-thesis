"""
def Find_Max_Length(list1):
    max_length = 0
    for i in range(len(list1)):
        length = 0
        for j in range(len(list1[i])):
            length += 1
        if length > max_length:
            max_length = length
    return max_length
"""

def Find_Max_Length(list1):
    max_length = 0
    for i in list1:
        max_length = max(max_length, len(i))
    return max_length

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

#from nose.tools import assert_equal
#assert_equal(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

"""
def Find_Max_Length(list1):
    max_length = 0
    for i in range(len(list1)):
        length = 0
        for j in range(len(list1[i])):
            length += 1
        if length > max_length:
            max_length = length
    return max_length
"""

def Find_Max_Length(list1):
    max_length = 0
    for i in list1:
        max_length = max(max_length, len(i))
    return max_length

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

#from nose.tools import assert_equal
#assert_equal(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

"""
def Find_Max_Length(list1):
    max_length = 0
    for i in range(len(list1)):
        length = 0
        for j in range(len(list1[i])):
            length += 1
        if length > max_length:
            max_length = length
    return max_length
"""

def Find_Max_Length(list1):
