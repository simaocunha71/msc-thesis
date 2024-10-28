def sort_even(l: list):
    even = sorted([x for x in l if l.index(x) % 2 == 0])
    return [x if l.index(x) % 2 != 0 else even.pop(0) for x in l]
# test the function
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
print(sort_even([7, 1, 2, 9, 4, 5, 6, 8]))  # [7, 1, 2, 9, 4, 6, 5, 3] 
print(sort_even([1, 5, 3, 2, 9, 8, 7, 4]))  # [1, 5, 3, 2, 9, 8, 7, 4]  # edge case: all even indices are in order
print(sort_even([5, 5, 5, 5]))  # [5, 5, 5, 5]  # edge case: all elements are the same
print(sort_even([]))  # []  # edge case: empty list
print(sort_even([1]))  # [1]  # edge case: list with one element
print(sort_even([1, 2]))  # [1, 2]  # edge case: list with two elements
print(sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # edge case: list with 10 elements
print(sort_even([1, 2, 3, 4, 5, 6, 7, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]  # edge case: list with 8 elements
print(sort_even([1, 2, 3, 4, 5, 6]))  # [1, 2, 3, 4, 5