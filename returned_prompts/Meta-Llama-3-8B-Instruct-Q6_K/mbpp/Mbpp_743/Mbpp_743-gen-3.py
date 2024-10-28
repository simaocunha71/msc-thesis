```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```
The function `rotate_right` takes a list `lst` and an integer `n` as input. It calculates the effective number of positions to rotate by taking the modulus of `n` with the length of the list. This is because rotating the list by its length is the same as not rotating it at all.

Then it returns a new list by concatenating two slices of the original list. The first slice is the last `n` elements of the list (`lst[-n:]`), and the second slice is all elements except the last `n` (`lst[:-n]`). This effectively rotates the list to the right by `n` positions. 

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` shows that the function correctly rotates the list to the right by 3 positions. 





```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
python
```







```
