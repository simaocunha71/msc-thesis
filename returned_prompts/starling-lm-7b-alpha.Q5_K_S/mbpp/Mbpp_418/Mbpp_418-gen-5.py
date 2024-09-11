"""
def Find_Max(my_list):
    if not my_list:
        return None
    max_length = len(my_list[0])
    max_index = 0
    for index, item in enumerate(my_list):
        if len(item) > max_length:
            max_length = len(item)
            max_index = index
    return my_list[max_index]
"""

# 更优解法
def Find_Max(my_list):
    if not my_list:
        return None
    max_length = 0
    max_index = 0
    for index, item in enumerate(my_list):
        if len(item) > max_length:
            max_length = len(item)
            max_index = index
    return my_list[max_index]

# assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
# assert Find_Max([]) == None
# assert Find_Max(['A', 'B', 'C']) == 'B'
# assert Find_Max([1, 2, 3]) == 3
# assert Find_Max([[1, 2, 3], ['A', 'B', 'C']]) == ['A', 'B', 'C']
# assert Find_Max([[1, 2, 3], ['A', 'B', 4], ['A', 'B', 'C']]) == ['A', 'B', 'C']
# assert Find_Max([[1, 2, 3], ['A', 'B', 'C'], ['A', 'B', 4]]) == ['A', 'B', 'C']
# assert Find_Max([[1, 2, 3], ['A', 'B', 'C'], ['A', 'B', 4], ['A', 'B', 'C', 5]]) == ['A', 'B', 'C', 5]
# assert Find_Max([]) == None

# 更优解法
def Find_Max_v2(my_list):
    if not my_list:
        return None
    max_length