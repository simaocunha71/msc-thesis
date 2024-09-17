```
def find_first_occurrence(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1
```
This function iterates over the array and returns the index of the first occurrence of the target number. If the target number is not found, it returns -1. The unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` ensures that the function works correctly. 





