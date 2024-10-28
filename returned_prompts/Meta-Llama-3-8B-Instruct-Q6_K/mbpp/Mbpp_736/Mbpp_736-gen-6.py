The problem is asking for a function that takes a sorted list and a value as input, and returns the index where the value should be inserted to maintain the sorted order.

From the given unit test `assert left_insertion([1,2,4,5],6)==4`, we can understand that the function should return the index where the value 6 should be inserted in the list [1,2,4,5] to maintain the sorted order. 

Here is the Python solution for the problem:
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
This function uses a binary search algorithm to find the insertion point. It initializes two pointers, `left` and `right`, to the start and end of the array, respectively. It then calculates the middle index `mid` and compares the value at `mid` with the input value `val`. If `arr[mid]` is less than `val`, it means the value should be inserted to the right of `mid`, so it updates `left` to `mid + 1`. If `arr[mid]` is greater than or equal to `val`, it means the value should be inserted to the left of `mid`, so it updates `right` to `mid - 1`. The process is repeated until `left` is greater than `right`. The final value of `left` is the insertion point. 