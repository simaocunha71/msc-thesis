def sort_even(l: list):
    return [i if i % 2 != 0 else sorted([x for x in l if x % 2 == 0])[l.index(x)] for i in l]

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]  # 4 should be 4, not 2
# print(sort_even([3, 1, 4]))  # [3, 1, 2]  # 3 is odd, 1 is odd, 4 is even, should be [3, 1, 2]
print(sort_even([3, 1, 4, 2]))  # [3, 1, 2, 4]  # 3 is odd, 1 is odd, 4 is even, 2 is even, should be [3, 1, 2, 4]
print(sort_even([1, 3, 5, 7]))  # [1, 3, 5, 7]  # all odd, should be [1, 3, 5, 7]
print(sort_even([2, 4, 6, 8]))  # [2, 4, 6, 8]  # all even, should be [2, 4, 6, 8]
print(sort_even([1, 2, 3, 4, 5, 6, 7, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]  # 1, 3, 5, 7 are odd, 2, 4, 6, 8 are even, should be [1, 2, 3, 4, 5, 6, 7, 8]
print(sort_even([1, 1, 1, 1]))  # [1, 1, 1, 1]  # all odd, should be [1, 1, 1, 1]
print(sort_even([2, 2, 2, 2]))  # [2, 2, 2, 2