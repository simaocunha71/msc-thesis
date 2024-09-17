```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```


The problem is asking you to write a function that rotates a given list by a specified number of items to the right direction. 

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` helps to clarify the problem. 

The function `rotate_right` takes two parameters: the list to be rotated and the number of items to rotate to the right. It returns the rotated list. 

The function uses list slicing to achieve the rotation. It takes the last `n` items of the list and moves them to the front of the list, effectively rotating the list to the right. The `%` operator is used to handle cases where `n` is greater than the length of the list. 

Here is the solution:
```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```


This function works by first calculating the actual number of items to rotate by taking the remainder of `n` divided by the length of the list. This is done to handle cases where `n` is greater than the length of the list. 

Then, it uses list slicing to take the last `n` items of the list and moves them to the front of the list. The `lst[-n:]` slice takes the last `n` items of the list, and the `lst[:-n]` slice takes all items except the last `n` items. By concatenating these two slices, the function effectively rotates the list to the right. 

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` demonstrates that the function works correctly. 

The function can be used to rotate a list by any number of items to the right. For example, `rotate_right([1, 2, 3, 4, 5