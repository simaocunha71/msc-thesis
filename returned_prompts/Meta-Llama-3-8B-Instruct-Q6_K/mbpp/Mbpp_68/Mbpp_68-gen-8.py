```
def is_Monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            decreasing = False
        if arr[i-1] < arr[i]:
            increasing = False
    return increasing or decreasing
```
The function `is_Monotonic` checks whether the given array is monotonic or not. It uses two boolean variables `increasing` and `decreasing` to track whether the array is increasing or decreasing respectively. 

It iterates through the array from the second element to the end, comparing each element with the previous one. If the current element is less than the previous one, it sets `increasing` to `False`. If the current element is greater than the previous one, it sets `decreasing` to `False`. 

Finally, it returns `True` if the array is either increasing or decreasing, and `False` otherwise. The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` suggests that the array is considered monotonic if it is either increasing or decreasing. 

For example, the array `[6, 5, 4, 4]` is considered monotonic because it is decreasing. The array `[1, 2, 3, 4]` is also considered monotonic because it is increasing. The array `[1, 2, 3, 2]` is not considered monotonic because it is neither increasing nor decreasing. 





