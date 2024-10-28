```
def is_Monotonic(arr):
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return True
    else:
        return False
```
This function checks if the given array is monotonic by comparing it with its sorted version. If the array is equal to its sorted version or its reverse sorted version, then it is monotonic. If not, then it is not monotonic. This function works for both increasing and decreasing monotonic arrays.

The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` is used to check if the function works correctly. The array `[6, 5, 4, 4]` is a monotonic array since it is sorted in ascending order. The function `is_Monotonic` should return `True` for this array. 







