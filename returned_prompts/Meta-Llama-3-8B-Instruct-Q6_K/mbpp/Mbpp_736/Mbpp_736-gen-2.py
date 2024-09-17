```
def left_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
The problem is asking to find the leftmost position where a specified value can be inserted in a sorted array to maintain the sorted order. This is a common problem in algorithms and data structures, and it can be solved using binary search.

The given unit test `assert left_insertion([1,2,4,5],6)==4` suggests that the function should return the index where the value 6 should be inserted in the sorted array [1,2,4,5] to maintain the sorted order.

Here's the solution:
```
def left_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
This function works by initializing two pointers, `left` and `right`, to the start and end of the array respectively. Then, it enters a loop where it calculates the midpoint of the current range and compares the value at the midpoint to the target value. If the value at the midpoint is less than the target value, it updates the `left` pointer to be the midpoint + 1. If the value at the midpoint is greater than or equal to the target value, it updates the `right` pointer to be the midpoint - 1. The loop continues until `left` is greater than `right`. The function then returns `left`, which is the leftmost position where the target value can be inserted to maintain the sorted order.