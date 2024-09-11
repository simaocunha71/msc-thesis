"""
def min_k(tuple_list, k):
    return sorted(tuple_list, key = lambda x: x[1])[:k]
"""

def min_k(tuple_list, k):
    tuple_list.sort(key = lambda x: x[1])
    return tuple_list[:k]

# assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]



