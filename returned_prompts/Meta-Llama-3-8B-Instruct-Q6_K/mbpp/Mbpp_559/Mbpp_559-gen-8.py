```
def max_sub_array_sum(lst, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(lst)):
        current_sum += lst[i]
        if i >= n:
            current_sum -= lst[i-n]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
```


Explanation:
The problem asks to find the sum of the largest contiguous sublist in the given list. This can be done by iterating through the list and maintaining a running sum of the current sublist. When the size of the current sublist exceeds n, we subtract the oldest element from the running sum. The maximum sum encountered during this process is the answer.

The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` suggests that the function should be able to find the maximum sum of a sublist of size n. Therefore, we need to modify the function to take an additional parameter n, which specifies the size of the sublist. If the size of the current sublist exceeds n, we subtract the oldest element from the running sum.

The time complexity of this solution is O(n), where n is the length of the list. The space complexity is O(1), as we only use a constant amount of space to store the maximum sum and the current sum.