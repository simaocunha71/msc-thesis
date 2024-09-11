"""
def two_unique_nums(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

