"""
def extract_singly(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, tuple):
            new_lst.extend(i)
        else:
            new_lst.append(i)
    return set(new_lst)
"""

# 2. Write a function to count the number of occurrences of each element in a list.
# 