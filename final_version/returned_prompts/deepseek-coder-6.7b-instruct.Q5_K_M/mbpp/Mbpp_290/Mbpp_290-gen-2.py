def max_length(lst):
    max_len = max(len(lst[i]) for i in range(len(lst)))
    max_lst = [lst[i] for i in range(len(lst)) if len(lst[i]) == max_len]
    return max_len, max_lst[0]

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""
Explanation:
The function max_length takes a list of lists as input. It calculates the maximum length of a sublist using a list comprehension. Then it constructs a list of sublists which have this maximum length. The function returns the maximum length and the first sublist of this list.
"""

# 