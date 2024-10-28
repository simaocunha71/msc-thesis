```
def is_majority(arr, n, element):
    if n <= 0:
        return False
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count > n // 2
```


The function `is_majority` takes three parameters: a sorted array `arr`, its length `n`, and an element to check. It returns a boolean indicating whether the given element is the majority element in the array.

The function first checks if the array length `n` is less than or equal to 0. If it is, the function returns `False` since there can't be a majority element in an empty array.

Then, it iterates over the array to count the occurrences of the given element. If the count is greater than `n // 2`, the function returns `True`, indicating that the element is the majority element. Otherwise, it returns `False`.

The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` confirms that the function works correctly. In this test, the element `3` occurs more than `n // 2` times in the array, so the function returns `True`. If the element occurred less than `n // 2` times, the function would return `False`.