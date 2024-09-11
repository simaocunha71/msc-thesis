def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return (max_len, max_list)

# test
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))  # (3, [13, 15, 17])

"""
def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return (max_len, max_list)

# test
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))  # (3, [13, 15, 17])
"""

def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return (max_len, max_list)

# test
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))  # (3, [13, 15, 17])

"""
def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return (max_len, max_list)

# test
print(max_length([[0], [