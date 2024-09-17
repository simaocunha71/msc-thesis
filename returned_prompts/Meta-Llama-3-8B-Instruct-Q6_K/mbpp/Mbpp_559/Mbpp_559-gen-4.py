```
def max_sub_array_sum(arr, k):
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum
```
The function `max_sub_array_sum` takes a list of numbers `arr` and an integer `k` as input and returns the sum of the largest contiguous sublist of length `k`. It maintains a sliding window of size `k` and updates the maximum sum as it slides through the list. The time complexity is O(n), where n is the length of the input list, and the space complexity is O(1). The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` checks that the function returns the correct sum for a given list and window size.