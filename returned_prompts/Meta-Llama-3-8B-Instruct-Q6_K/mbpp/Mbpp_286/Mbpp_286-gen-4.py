```
def max_sub_array_sum_repeated(arr, k, n):
    repeated_arr = arr * k
    max_sum = float('-inf')
    for i in range(len(repeated_arr)):
        for j in range(i, len(repeated_arr)):
            window_sum = sum(repeated_arr[i:j+1])
            max_sum = max(max_sum, window_sum)
    return max_sum
```


This function works by first creating a new array that is the input array repeated k times. It then iterates over the new array to find the maximum sum of any contiguous subarray. It does this by iterating over the array and calculating the sum of each subarray. It keeps track of the maximum sum found so far and returns it at the end. The time complexity of this function is O(n^2), where n is the length of the input array. The space complexity is O(1), as it only uses a constant amount of space to store the maximum sum and the window sum.  This function is tested with the provided unit test, which verifies that it returns the correct result for the given input.