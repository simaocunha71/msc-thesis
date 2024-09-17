```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```


The function takes a list and an integer as arguments. The integer represents the number of items to rotate the list to the right. The function returns the rotated list.

The function works by slicing the list into two parts: the last `n` elements and the rest of the list. The `n` elements are moved to the beginning of the list, effectively rotating the list to the right. The `%` operator is used to ensure that `n` is within the bounds of the list length, in case `n` is greater than the list length.

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` checks that the function correctly rotates the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` by 3 items to the right. The expected output is `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`, which is the result of rotating the original list by 3 items to the right.