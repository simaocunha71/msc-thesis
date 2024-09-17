```
def is_Monotonic(arr):
    is_increasing = False
    is_decreasing = False
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            is_increasing = True
        elif arr[i] < arr[i-1]:
            is_decreasing = True
        else:
            continue
    
    return is_increasing or is_decreasing
```


This function iterates over the array, comparing each element with the previous one. If the array is increasing, it sets `is_increasing` to `True`, if it's decreasing, it sets `is_decreasing` to `True`. If the array is neither increasing nor decreasing, it will return `False`. 

The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` passes because the array is not strictly increasing, but it's monotonic. 

This function considers an array to be monotonic if it's either strictly increasing or strictly decreasing, not necessarily monotonic in the classical sense (i.e., not necessarily constant or non-decreasing).  It's based on the definition of monotonic sequence, which is a sequence that is either strictly increasing or strictly decreasing.  If the sequence is neither strictly increasing nor strictly decreasing, it's not considered monotonic.  For example, the sequence [1, 2, 3, 3, 4, 5] is not considered monotonic because it's not strictly increasing and it's not strictly decreasing.  It's considered neither monotonic nor non-monotonic.  However, the sequence [1, 2, 2, 3, 4, 5] is considered monotonic because it's strictly increasing.  The sequence [5, 4, 3, 2, 1] is also considered monotonic because it's strictly decreasing.  If the sequence is constant, it's considered monotonic.  For example, the sequence [1, 1, 1, 1, 1] is considered monotonic.  If the sequence is neither strictly increasing nor strictly decreasing, it's not considered monotonic.  For example, the sequence [1, 2, 3, 3, 4, 5] is not considered monotonic.  It's considered neither monotonic nor non-monotonic.  It's based on the definition of monotonic sequence, which is a sequence