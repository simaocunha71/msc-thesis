def min_k(lst, k):
    return sorted(lst, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2))  # [('Akash', 2), ('Akshat', 4)]


This function works by sorting the list of tuples based on the second element of the tuple (which is the value). Then it returns the first k elements of the sorted list, which are the k smallest values.

The test case provided is:
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]

This test case checks if the function returns the correct result for a given input. The function should return the two smallest values, which are [('Akash', 2), ('Akshat', 4)]. The function passes this test case. 





# Python3 solution
def min_k(lst, k):
    return sorted(lst, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2))  # [('Akash', 2), ('Akshat', 4)]


# Python 2.7 solution
def min_k(lst, k):
    return sorted(lst, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2))  # [('Akash', 2), ('Akshat', 4)]


Both Python3 and Python2.7 solutions work because they use the built-in sorted function with a key function that sorts the list based on the second element of the tuple. The function then returns the first k elements of the sorted list, which are the k smallest values. 