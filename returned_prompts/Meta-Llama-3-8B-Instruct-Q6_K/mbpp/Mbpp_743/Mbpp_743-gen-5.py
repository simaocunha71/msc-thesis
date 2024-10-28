```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```


The function `rotate_right` takes a list `lst` and an integer `n` as input, and returns a new list that is the result of rotating `lst` to the right by `n` positions. The rotation is done by slicing the list into two parts: the last `n` elements and the rest of the list, and then concatenating them in reverse order. The `%` operator is used to ensure that `n` is within the range of the list's length, so that the rotation wraps around correctly. For example, if the list has 10 elements and `n` is 11, the function will rotate the list by 1 position, because `11 % 10` is 1. The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` checks that the function correctly rotates the list by 3 positions to the right.