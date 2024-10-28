The problem asks to create a function that calculates the sum of all subarrays with odd lengths in a given array. 

However, the problem statement doesn't specify whether the subarrays should be contiguous or not. 

Fortunately, the unit test `assert odd_length_sum([1,2,4]) == 14` provides a hint. It suggests that the subarrays can be any odd-length subsequence of the array, not necessarily contiguous.

Here is a Python solution for this problem:

```Python
def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) % 2 != 0:
                total_sum += sum(arr[i:j+1])
    return total_sum
```

This function generates all possible subarrays of the given array, checks if the length of each subarray is odd, and if it is, adds the sum of that subarray to the total sum. The function finally returns the total sum. 

The time complexity of this function is O(n^2) where n is the length of the input array. This is because it generates all possible subarrays, which takes O(n^2) time, and for each subarray, it calculates the sum, which takes O(n) time. The space complexity is O(1) as it only uses a constant amount of space to store the total sum and the indices of the subarrays. 