"""
def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

# def count_element_in_list(lst, element):
#     count = 0
#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             if lst[i][j]==element:
#                 count += 1
#     return count

# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

# def count_element_in_list(lst, element):
#     count = 0
#     for sublist in lst:
#         if element in sublist:
#             count += 1
#     return count

# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

# def count_element_in_list(lst, element):
#     count = 0
#     for i, sublist in enumerate(lst):
#         if element in sublist:
#             count += 1
#     return count

# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3

#