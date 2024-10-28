def Extract(lst):
    return [i[0] for i in lst]
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))  # Output: [1, 3, 6]  # test the function
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]  # test the function
print(Extract([[1], [2, 3], [4, 5, 6]]))  # Output: [1, 2, 4]
assert Extract([[1], [2, 3], [4, 5, 6]]) == [1, 2, 4]  # test the function
print(Extract([[1, 2], [3, 4], [5, 6, 7]]))  # Output: [1, 3, 5]
assert Extract([[1, 2], [3, 4], [5, 6, 7]]) == [1, 3, 5]  # test the function
print(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 4, 7]
assert Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 7]  # test the function
print(Extract([[1], [2], [3]]))  # Output: [1, 2, 3]
assert Extract([[1], [2], [3]]) == [1, 2, 3]  # test the function
print(Extract([[1, 2], [3, 4], [5, 6]]))  # Output: [1, 3, 5]
assert Extract([[1, 2], [3, 4], [5, 6]]) == [1, 3, 5]  # test the function
print(Extract([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 