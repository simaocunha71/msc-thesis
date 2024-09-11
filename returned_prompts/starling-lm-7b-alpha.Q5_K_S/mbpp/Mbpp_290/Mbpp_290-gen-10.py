"""
def max_length(input_list):
    return max(input_list, key = len)
"""

def max_length(input_list):
    max_length = 0
    max_list = []
    for i in input_list:
        if len(i) > max_length:
            max_length = len(i)
            max_list = i
    return max_length, max_list

assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])

# Made By Mostafa_Khaled
```