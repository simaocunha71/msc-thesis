```
def check_min_heap(arr):
    if len(arr) < 1:
        return True
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[i] > arr[left]:
            return False
        if right < len(arr) and arr[i] > arr[right]:
            return False
    return True
```


This function checks if the given array represents a min heap by iterating over each element and its children. If the parent is greater than either of its children, it means the array is not a min heap and the function returns False. If the function doesn't find any such parent-child relationship, it means the array is a min heap and the function returns True. The base case for the recursion is when the array is empty, in which case the function returns True.

The unit test `assert check_min_heap([1, 2, 3, 4, 5, 6]) == True` ensures that the function correctly identifies a min heap. It checks if the given array is a min heap and expects the function to return True. If the function returns anything other than True, the test will fail.