def rotate_right(lst, k):
    return lst[-k:] + lst[:-k]

# test the function
print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))
# output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

"""
Explanation:
The function `rotate_right` takes a list and a number `k` as arguments. It slices the list into two parts at the index `k` from the end.
It then concatenates these two parts in reverse order.
"""

