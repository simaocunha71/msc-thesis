def rotate_right(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
The function rotate_right takes a list and a number k as input. The list is rotated to the right by k items by splitting the list at the end -k items and the beginning -(end-k) items and then concatenating the two parts in the reverse order.
"""

"""
Output: 
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""

#Testing
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],10)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],20)==[1, 2, 3, 4, 5