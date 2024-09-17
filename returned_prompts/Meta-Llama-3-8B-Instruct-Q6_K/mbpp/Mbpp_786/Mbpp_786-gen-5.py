The problem is asking for a function that finds the correct position to insert a given value into a sorted list, so that the list remains sorted.

Here is a Python solution for this problem:

```python
def right_insertion(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return low
```

This function uses a binary search algorithm to find the correct position. It starts by considering the middle element of the list. If the middle element is less than the given value, it moves the low pointer to the right of the middle element. If the middle element is greater than or equal to the given value, it moves the high pointer to the left of the middle element. This process continues until the low pointer is greater than the high pointer, at which point the low pointer indicates the correct position to insert the given value. 

For example, if we have the list [1,2,4,5] and we want to insert 6, the function will return 4, which is the correct position to insert 6 so that the list remains sorted. 