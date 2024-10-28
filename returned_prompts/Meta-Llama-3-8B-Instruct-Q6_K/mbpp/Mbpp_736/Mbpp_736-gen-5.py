```
def left_insertion(arr, value):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
This function uses a binary search approach to find the left insertion point for a specified value in a sorted array. It iteratively narrows down the search range until it finds the leftmost position where the value can be inserted while maintaining the sorted order.

The unit test `assert left_insertion([1,2,4,5],6)==4` confirms that the function correctly returns the left insertion point for the value 6 in the array [1,2,4,5], which is 4. This is because 6 should be inserted at the end of the array to maintain the sorted order.