```
def get_max_sum(n):
    # Initialize the array with 0
    max_sum = [0] * (n + 1)

    # For each number, calculate the maximum sum
    for i in range(1, n + 1):
        if i % 2 == 0:
            max_sum[i] = max_sum[i // 2] + max_sum[i // 2] + 1
        elif i % 3 == 0:
            max_sum[i] = max_sum[i // 3] + max_sum[i // 3] + 1
        elif i % 4 == 0:
            max_sum[i] = max_sum[i // 4] + max_sum[i // 4] + 1
        elif i % 5 == 0:
            max_sum[i] = max_sum[i // 5] + max_sum[i // 5] + 1
        else:
            max_sum[i] = i

    return max_sum[n]
```

This function uses a dynamic programming approach to calculate the maximum sum for each number. It initializes an array `max_sum` with all 0s, then iterates over each number from 1 to `n`. For each number, it checks if the number is divisible by 2, 3, 4, or 5. If it is, it adds the maximum sum of the corresponding divisor to the previous maximum sum and adds 1. If the number is not divisible by any of these numbers, it simply sets the maximum sum to be the number itself. Finally, it returns the maximum sum for the given `n`.

For example, if `n` is 60, the function will calculate the maximum sum as follows:

```python
max_sum = [0, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 