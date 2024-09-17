The problem is asking for a function that finds the sum of the largest contiguous sublist in a given list. However, it seems like there's an additional condition that's not explicitly mentioned in the problem statement. 

The condition is that the sum should be less than or equal to a given number. This condition is not mentioned in the problem statement, but it's included in the unit test provided. The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` implies that the sum should be less than or equal to 8.

Here's the solution for the problem:

```
def max_sub_array_sum(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    left = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
```

This function uses a sliding window approach to find the maximum sum of a contiguous sublist. It maintains a `current_sum` variable that keeps track of the sum of the current window, and a `left` variable that represents the starting index of the window. It then iterates through the array, adding elements to the `current_sum` and moving the `left` index to the right when the sum exceeds the given number `k`. The maximum sum found is returned as the result. 