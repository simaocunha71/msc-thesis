```
def right_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
```    
The function `right_insertion` takes a sorted list `arr` and a value `val` as input. It returns the index where `val` should be inserted to maintain the sorted order. If `val` is already present in the list, the function returns the index of `val`. If `val` is not present, the function returns the index where `val` should be inserted to maintain the sorted order.

The function uses a binary search approach to find the right insertion point. It maintains two pointers, `left` and `right`, which represent the range of the list to be searched. Initially, `left` is set to 0 and `right` is set to the last index of the list.

The function then calculates the midpoint `mid` of the range and compares the value at the midpoint with `val`. If `arr[mid]` is equal to `val`, the function returns the index `mid`. If `arr[mid]` is less than `val`, the function updates `left` to `mid + 1` to narrow down the search range. If `arr[mid]` is greater than `val`, the function updates `right` to `mid - 1` to narrow down the search range.

The function continues this process until `left` is greater than `right`. At this point, `left` is the index where `val` should be inserted to maintain the sorted order. If `val` is not present in the list, the function returns `left`. If `val` is already present in the list, the function returns the index of `val`.

The unit test `assert right_insertion([1,2,4,5],6)==4` ensures that the function returns the correct index when the value is not present in the list. The function should return 4, which is the index where 6 should be inserted to maintain the sorted order.