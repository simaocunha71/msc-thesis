def Find_Max(lst):
    max_len = -1
    max_lst = []
    for l in lst:
        if len(l) > max_len:
            max_len = len(l)
            max_lst = l
    return max_lst

print(Find_Max([['A'],['A','B'],['A','B','C']]))

"""
output:
['A', 'B', 'C']
"""

Explanation:
The function iterates over each sublist in the given list. It checks the length of each sublist and if it is greater than the current maximum length, it updates the maximum length and sets the corresponding sublist as the maximum sublist. Finally, it returns the sublist with maximum length.
"""

