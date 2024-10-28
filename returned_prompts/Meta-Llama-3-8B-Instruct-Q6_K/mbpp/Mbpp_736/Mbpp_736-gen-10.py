```
def left_insertion(arr, value):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
The function `left_insertion` takes a sorted array `arr` and a value `value` as input. It returns the left insertion point for the value in the sorted array.

The function uses a binary search approach to find the left insertion point. It initializes two pointers, `left` and `right`, to the start and end of the array, respectively. Then, it enters a loop that continues until `left` is greater than `right`.

In each iteration of the loop, the function calculates the middle index `mid` and compares the value at `mid` with the specified value `value`. If the value at `mid` is less than `value`, it updates `left` to `mid + 1`. If the value at `mid` is greater than or equal to `value`, it updates `right` to `mid - 1`.

The loop continues until `left` is greater than `right`. At this point, `left` is the left insertion point for the value in the sorted array.

The unit test `assert left_insertion([1,2,4,5],6)==4` ensures that the function returns the correct left insertion point for the value 6 in the sorted array [1,2,4,5]. The expected output is 4, which is the correct left insertion point for the value 6 in the sorted array. 