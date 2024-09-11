"""
def min_k(data, k):
    # Sorting the list by the second element of the tuple
    data.sort(key=lambda x: x[1])
    # Returning the first k elements
    return data[:k]
"""

def min_k(data, k):
    # Sorting the list by the second element of the tuple
    data.sort(key=lambda x: x[1])
    # Returning the first k elements
    return data[:k]


"""
Here are some of the test cases to test the function

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 1) == [('Akash', 2)]
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 0) == []
assert min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 0) == []
assert min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 1) == [(1, 1)]
assert min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 2) == [(1, 1), (2, 2)]
assert min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 3) == [(1, 1), (2, 2), (3, 3)]
assert min_k([(1, 1), (2, 2), (3, 3), (4, 4)], 4) == [(1