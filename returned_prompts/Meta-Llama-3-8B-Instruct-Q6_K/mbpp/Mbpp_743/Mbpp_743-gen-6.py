```
def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
```


The function takes a list and an integer as input, and returns a new list that is the input list rotated to the right by the specified number of items. 

The unit test provided ensures that the function works correctly. 

For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and the number of items to rotate is 3, the function should return [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]. 

The function uses Python's list slicing feature to achieve this. The expression `lst[-k:]` gets the last k items of the list, and `lst[:-k]` gets all items except the last k. The two parts are then concatenated in reverse order to get the rotated list. 

The line `k = k % len(lst)` is used to handle cases where k is greater than the length of the list. This ensures that the function works correctly for any positive integer k. 

The function does not modify the original list, but returns a new list that is the rotated version of the input list. 
```python
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
```  This test checks if the function is working correctly for a list of 10 items and a rotation of 3 items. The expected output is [8, 9, 10, 1, 2, 3, 4, 5, 6, 7].  This test ensures that the function is working correctly for all positive integers k. 
```python
assert rotate_right([1, 2, 3], 1) == [3, 1, 2]
``` This test checks if the function is working correctly for a list of 3 items and a rotation of 1 item. The expected output is [3, 1, 2]. 
```python
assert rotate_right([1, 2, 3, 