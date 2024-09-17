The problem is asking for a Python function that counts the number of inversions in an array. An inversion is when a larger number appears before a smaller number in the array. For example, in the array [1,20,6,4,5], there are 5 inversions (20-6, 20-4, 20-5, 6-4, 6-5).

Here is the Python function that solves this problem:

```Python
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
```

This function works by iterating through each pair of elements in the array, and if the first element is greater than the second, it increments the inversion count. The time complexity of this function is O(n^2), where n is the size of the array. This is because it has a nested loop structure, which is the most time-consuming operation in this function.

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` ensures that the function returns the correct number of inversions for the given array. This test is useful for checking if the function is working correctly, especially when the problem is complex and there are many edge cases.