```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff
```
This function first sorts the given array in ascending order. Then it iterates over the array from the second element to the last element (inclusive), calculates the difference between the current element and the previous element, and updates the minimum difference if the current difference is smaller. Finally, it returns the minimum difference.

For example, if the input array is `(1,5,3,19,18,25)` and the size of the array is `6`, the function will return `1`, which is the minimum difference between any two elements in the array. The elements `3` and `5` have a difference of `1`, which is the smallest difference between any two elements in the array. 

The unit test `assert find_min_diff((1,5,3,19,18,25),6) == 1` ensures that the function works correctly. 

The time complexity of this function is O(n log n) due to the sorting operation, where `n` is the size of the input array. The space complexity is O(1) as it only uses a constant amount of space to store the minimum difference and the indices. 