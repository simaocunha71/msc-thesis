def rotate_right(lst,n):
    return lst[-n:] + lst[:-n]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
Explanation:
The function rotate_right takes in a list and a number n. It returns a new list which is a rotation of the original list. The rotation is performed by taking the last n elements of the original list and appending them at the beginning of the list. Then, it takes the first elements of the original list which are not included in the rotation and appends them at the end of the list.
"""
<jupyter_output>
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
2. Write a Python function to remove duplicates from a list while preserving the order.
<jupyter_code>
