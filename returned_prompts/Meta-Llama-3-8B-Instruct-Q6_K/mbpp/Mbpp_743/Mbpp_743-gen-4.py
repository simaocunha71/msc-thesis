```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```


This function takes a list and a number of positions to rotate as input. It calculates the actual number of positions to rotate by taking the modulus of the input number with the length of the list. This is because rotating the list by its length is equivalent to not rotating it at all.

Then it returns a new list that is the concatenation of two slices of the input list. The first slice is from the end of the list to the position of the rotation (inclusive), and the second slice is from the beginning of the list to the position of the rotation. This effectively rotates the list to the right by the specified number of positions.

For example, if we call `rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)`, it will return `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`, which is the input list rotated 3 positions to the right. 





