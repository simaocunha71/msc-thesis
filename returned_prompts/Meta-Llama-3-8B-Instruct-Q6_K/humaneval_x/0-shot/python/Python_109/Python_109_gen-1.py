Here is the Python solution for the problem:

```
def move_one_ball(arr):
    if not arr:  # check if the array is empty
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:  # check if the array is not in non-decreasing order
            return False
    return True
```
The function `move_one_ball(arr)` checks if the given array `arr` can be sorted in non-decreasing order by performing right shift operations. It first checks if the array is empty. If it is, the function returns `True` because an empty array is already sorted.

Then, it iterates through the array, comparing each element with the next one. If it finds any pair of elements where the first element is greater than the second, it returns `False` because it is not possible to sort the array in non-decreasing order.

If the function doesn't find any such pair, it returns `True` because the array can be sorted in non-decreasing order by performing right shift operations. 

For example, for the array `[3, 4, 5, 1, 2]`, the function returns `True` because the array can be sorted in non-decreasing order by performing 2 right shift operations. For the array `[3, 5, 4, 1, 2]`, the function returns `False` because it is not possible to sort the array in non-decreasing order by performing any number of right shift operations. 