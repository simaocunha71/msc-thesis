def min_k(lst, k):
    lst = sorted(lst)
    return lst[:k]



# Test Cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
print("Test Case 1 Passed")

assert min_k([('Akash', 4), ('Manjeet', 10), ('Akshat', 2), ('Nikhil', 8)], 2) == [('Akash', 4), ('Akshat', 2)]
print("Test Case 2 Passed")

assert min_k([('Akash', 4), ('Manjeet', 10), ('Akshat', 2), ('Nikhil', 8)], 3) == [('Akash', 4), ('Akshat', 2), ('Manjeet', 10)]
print("Test Case 3 Passed")

# assert min_k([('A', 4), ('Manjeet', 10), ('Akshat', 2), ('Nikhil', 8)], 4) == [('A', 4), ('Akash', 2), ('Akshat', 2), ('Manjeet', 10)]
# print("Test Case 4 Passed")

# assert min_k([('A', 4), ('Manjeet', 10), ('Akshat', 2), ('Nikhil', 8)], 5) == [('A', 4), ('Akash', 2), ('Akshat', 2), ('Manjeet', 10), ('Nikhil', 8)]
# print("Test Case 5 Passed")

# assert min_k([('A', 4), ('Manjeet', 10), ('Akshat', 2), ('Nikhil', 8)], 0) == []
# print("Test Case 6 Passed")

# assert min