```
def is_majority(arr, n, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count > n // 2
```
This function iterates over the array and counts the occurrences of the target element. It then checks if the count is greater than n/2, which is the condition for the element to be the majority element. If the count is greater, it returns True, otherwise it returns False.

The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` confirms that the function works correctly. The target element 3 occurs more than n/2 times in the array, so the function returns True.