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


The problem is asking to find the sum of the largest contiguous sublist in the given list. 

The given unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` suggests that the input list is a 1D list of numbers, and the function should find the sum of the largest contiguous sublist in the given list.

Here is the Python solution for the problem. The function `max_sub_array_sum` takes a list `arr` and its length `n` as input, and returns the sum of the largest contiguous sublist in the given list.

The function uses two variables, `max_sum` and `current_sum`, to keep track of the maximum sum and the current sum of the contiguous sublist respectively. It iterates over the list, adding each element to `current_sum`. If `current_sum` is greater than `max_sum`, it updates `max_sum`. If `current_sum` is less than 0, it resets `current_sum` to 0. Finally, it returns `max_sum` which is the sum of the largest contiguous sublist in the given list. 





Note: 
The problem statement does not specify whether to consider negative numbers or not. However, based on the given unit test, it seems that we should consider all numbers, including negative numbers. Therefore, the function does not filter out negative numbers. If the problem statement is changed to consider only positive numbers, the function would need to be modified accordingly.