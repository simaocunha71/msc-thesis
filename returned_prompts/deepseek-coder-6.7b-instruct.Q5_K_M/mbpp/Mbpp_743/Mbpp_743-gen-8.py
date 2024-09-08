def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

Explanation:
In the function, we are using python slicing to rotate the list to the right. The slicing operation is [:-n] which gives us all elements in the list from start to n elements from the end, and lst[-n:] gives us last n elements of the list. By concatenating these two we get the rotated list.
"""

