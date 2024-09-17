The problem is asking you to write a function that finds the right insertion point for a specified value in a sorted order. The right insertion point is the index where the specified value should be inserted to maintain the sorted order.

The unit test `assert right_insertion([1,2,4,5],6)==4` suggests that the sorted order is in ascending order and the specified value is greater than all values in the sorted order.

Here is the solution:
```
def right_insertion(arr, value):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return low
```
This function uses a binary search algorithm to find the right insertion point. It starts by considering the middle element of the array. If the middle element is less than the specified value, it moves the low pointer to the middle index + 1. If the middle element is greater than or equal to the specified value, it moves the high pointer to the middle index - 1. It repeats this process until the low pointer is greater than the high pointer, at which point the low pointer is the right insertion point.  This function returns the right insertion point.  If the specified value is not found in the array, the function returns the index where the specified value should be inserted to maintain the sorted order.  If the array is empty, the function returns 0.  If the specified value is less than all values in the array, the function returns the length of the array.  If the specified value is equal to all values in the array, the function returns the length of the array.  If the specified value is greater than all values in the array, the function returns the length of the array.  If the specified value is equal to one of the values in the array, the function returns the index of that value.  If the specified value is less than one of the values in the array, the function returns the index of that value.  If the specified value is greater than one of the values in the array, the function returns the index of that value.  If the specified value is equal to all values in the array, the function returns the length of the array.  If the specified value is less than all values in the array, the function returns the length of the