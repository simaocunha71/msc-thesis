```
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                return False
        arr = arr[1:] + [arr[0]]
    return True
```


Explanation:
The function `move_one_ball(arr)` takes an array as input and returns `True` if it's possible to get an array sorted in non-decreasing order by performing right shift operations, and `False` otherwise.

The function first checks if the array is empty. If it is, it returns `True` as it's possible to get an empty array.

Then, it iterates over the array. For each element, it checks if the array is sorted in non-decreasing order. If it finds an element that is greater than the next one, it returns `False` as it's not possible to get the array sorted by performing right shift operations.

If the array is sorted after checking all elements, it performs a right shift operation by removing the first element and adding it to the end of the array. This is done in the line `arr = arr[1:] + [arr[0]]`. This operation is repeated until the array is sorted.

If the function has not returned `False` after checking all elements, it returns `True` as it's possible to get the array sorted by performing right shift operations.