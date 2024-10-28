```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```
The function takes a list and an integer `n` as input. It calculates the effective number of positions to rotate by taking the modulus of `n` with the length of the list. This is because rotating the list by its length is the same as not rotating it at all.

Then it returns a new list that is the concatenation of the last `n` elements of the original list and the rest of the elements. This effectively rotates the list to the right by `n` positions. The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` demonstrates this. The list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` is rotated to the right by 3 positions, resulting in `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`.  ```
```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```  ```
```
The function takes a list and an integer `n` as input. It calculates the effective number of positions to rotate by taking the modulus of `n` with the length of the list. This is because rotating the list by its length is the same as not rotating it at all.

Then it returns a new list that is the concatenation of the last `n` elements of the original list and the rest of the elements. This effectively rotates the list to the right by `n` positions. The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` demonstrates this. The list `[1, 2, 3, 4, 5, 6, 7, 8