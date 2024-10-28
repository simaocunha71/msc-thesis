```
def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
```
The function `max_sub_array_sum` takes a list `arr` and an integer `n` as input. It initializes `max_sum` to negative infinity and `current_sum` to 0. Then, it iterates over the list `arr` for `n` times. In each iteration, it adds the current element to `current_sum`. If `current_sum` is greater than `max_sum`, it updates `max_sum`. If `current_sum` becomes negative, it resets `current_sum` to 0. Finally, it returns `max_sum`. 

For example, if the input list is `[-2, -3, 4, -1, -2, 1, 5, -3]` and `n` is 8, the function returns `7` which is the sum of the largest contiguous sublist `4, -1, -2, 1, 5`. 

Note: The problem statement does not specify the size of the sublist, but based on the unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7`, it seems that the function should return the sum of the largest contiguous sublist of any size, not just the largest one of size `n`. In this case, the function can be simplified to only keep track of the maximum sum seen so far.  This is also the solution that the unit test is expecting.  The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` is expecting the sum of the largest contiguous sublist to be 7, which is the sum of the largest contiguous sublist in the list `[-2, -3, 4, -1, -2, 1, 5, -3]`.  This is a different problem than the original problem statement, but it is what the unit test is expecting.  The original problem statement asked for the largest contiguous sublist