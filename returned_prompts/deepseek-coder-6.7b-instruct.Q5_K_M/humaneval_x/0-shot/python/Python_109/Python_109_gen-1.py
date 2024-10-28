
def move_one_ball(arr):
    if not arr:
        return True
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count += 1
    if arr[-1] > arr[0]:
        count += 1
    return count <= 1
```

The function `move_one_ball` takes as input a list `arr` and checks if it is possible to sort the list by performing at most one right shift operation. The function counts the number of pairs of elements in `arr` that are in the wrong order and increments a counter if the last element of `arr` is greater than the first one. The function returns `True` if the counter is less or equal to 1, and `False` otherwise.

The time complexity of this function is O(n) as it iterates over the list `arr` once. The space complexity is O(1) as no additional space is used.

The function works by iterating over the list `arr` and comparing each element with its next one. If an element is greater than its next one, it means that the array is not sorted and a right shift operation is needed. The function also checks if the last element of `arr` is greater than the first one and increments the counter if it is. The function returns `True` if the counter is less or equal to 1, and `False` otherwise.

Here is a test with the provided examples:

```python
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```

The function `move_one_ball` works for any list of unique integers. It returns `True` if the list is empty or it is possible to sort the list by performing at most one right shift operation, and `False` otherwise.
"""

# Solution
def move_one_ball(arr):
    if not arr or len(arr) < 2:
        return True

    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i