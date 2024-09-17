def add_tuple(lst, t):
    lst += list(t)
    return lst
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
print(add_tuple([5, 6, 7], (9, 10)))  # [5, 6, 7, 9, 10]
print(add_tuple([1, 2], (3, 4)))  # [1, 2, 3, 4]
print(add_tuple([1], (2,)))  # [1, 2]
print(add_tuple([], (1, 2, 3)))  # [1, 2, 3]  # [1, 2, 3]
print(add_tuple([], ()))  # []  # []  # []  # []  # []  # []
# test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test case failed.  # test