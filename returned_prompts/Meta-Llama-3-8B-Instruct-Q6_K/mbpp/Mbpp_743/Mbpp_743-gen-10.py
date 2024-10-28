```
def rotate_right(lst, n):
    if n >= len(lst):
        n = n % len(lst)
    return lst[-n:] + lst[:-n]
```





In this function, we first check if the number of positions to rotate is greater than or equal to the length of the list. If it is, we take the remainder of the division of the number of positions by the length of the list. This is because rotating more than the length of the list is equivalent to rotating the remainder of the division.

Then we return the list by slicing it into two parts: the last n elements and the rest of the list. This effectively rotates the list to the right by n positions.