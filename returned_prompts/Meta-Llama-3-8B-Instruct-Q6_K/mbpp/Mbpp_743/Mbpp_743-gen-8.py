```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```
The function `rotate_right` takes a list `lst` and an integer `n` as input. It first calculates the effective number of positions to rotate by taking the modulus of `n` with the length of the list. This is to handle the case where `n` is greater than the length of the list. 

Then it slices the list into two parts: the last `n` elements and the rest of the list. The result is the concatenation of these two parts in reverse order, which effectively rotates the list to the right by `n` positions. 

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` demonstrates this functionality. 

For example, if we rotate the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` by 3 positions to the right, the result is `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`. 

The function works by taking the last 3 elements (`[8, 9, 10]`) and moving them to the front of the list, effectively rotating it to the right by 3 positions. 

This solution has a time complexity of O(1) as it only involves a constant amount of work to calculate the effective number of positions to rotate and to slice the list. The space complexity is also O(1) as it only uses a constant amount of space to store the result. 





Note: This function does not modify the original list, it returns a new list. If you want to modify the original list, you can use the following code:

```
def rotate_right(lst, n):
    n = n % len(lst)
    lst[:] = lst[-n:] + lst[:-n]
```

This code uses the slice assignment `lst[:] = ...` to modify the original list. The rest of the function is the same as before. 