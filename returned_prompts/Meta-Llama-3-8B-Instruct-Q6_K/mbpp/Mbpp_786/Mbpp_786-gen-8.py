```
def right_insertion(sorted_list, value):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
The function `right_insertion` takes two parameters: a sorted list `sorted_list` and a value `value`. It returns the index where the `value` should be inserted to keep the list sorted.

This function uses a binary search algorithm. It starts by setting two pointers, `left` and `right`, to the start and end of the list, respectively. It then enters a loop that continues until `left` is greater than `right`.

In each iteration of the loop, the function calculates the middle index `mid` and compares the value at that index to the `value`. If the value at `mid` is equal to the `value`, the function returns `mid`. If the value at `mid` is less than the `value`, the function updates `left` to `mid + 1`. If the value at `mid` is greater than the `value`, the function updates `right` to `mid - 1`.

Once the loop finishes, the function returns `left`, which is the index where the `value` should be inserted to keep the list sorted. If the `value` is not found in the list, the function returns the index where the `value` should be inserted to keep the list sorted.

The unit test `assert right_insertion([1,2,4,5],6)==4` ensures that the function correctly returns the index where the value 6 should be inserted to keep the list sorted. In this case, the function returns 4, which is the correct index.