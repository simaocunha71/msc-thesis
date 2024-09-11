def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return max_len, max_list


# def max_length(l):
#     max_len = 0
#     max_list = []
#     for i in l:
#         if len(i) > max_len:
#             max_len = len(i)
#             max_list = i
#     return max_len, max_list

# print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))


def max_length(l):
    return max(l, key=len)

# print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

def max_length(l):
    return max(l, key=len), l.index(max(l, key=len))

# print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

def max_length(l):
    max_list = l[0]
    for sublist in l:
        if len(sublist) > len(max_list):
            max_list = sublist
    return len(max_list), max_list

# print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))





































































