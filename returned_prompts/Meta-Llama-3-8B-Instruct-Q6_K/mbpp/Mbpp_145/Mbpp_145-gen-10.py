```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


Explanation:
The function `max_Abs_Diff` takes an array as input and returns the maximum absolute difference between any two elements in the array. This is achieved by subtracting the minimum element from the maximum element in the array. The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` ensures that the function works correctly for the given input. The time complexity of this function is O(n), where n is the number of elements in the array, because it needs to find the minimum and maximum elements in the array. The space complexity is O(1), as it only uses a constant amount of space to store the minimum and maximum elements.