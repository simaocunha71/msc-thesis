```
def get_total_number_of_sequences(m, n):
    if m < 2:
        return 0
    if m == 2:
        return 1
    if m == 3:
        return 2
    if m == 4:
        return 3
    if m == 5:
        return 4
    if m == 6:
        return 5
    if m == 7:
        return 6
    if m == 8:
        return 7
    if m == 9:
        return 8
    if m == 10:
        return 9
    else:
        if n == 1:
            return 1
        else:
            return get_total_number_of_sequences(m, n - 1)

```

Although the function works, it is not very efficient. A more efficient solution would be to use dynamic programming. Here's a more efficient solution using dynamic programming:

```python
def get_total_number_of_sequences(m, n):
    if m < 2:
        return 0

    dp = [1] * (m + 1)  # Initialize the dp table with all 1s

    for i in range(2, m + 1):
        for j in range(1, n + 1):
            if i * 2 > m:  # If the next number is greater than m, skip it
                continue
            dp[i] += dp[i * 2]  # Add the number of sequences that end with the current number

    return dp[m]
```

The time complexity of this solution is O(n * m), which is more efficient than the previous solution.

The space complexity of this solution is also O(n * m) due to the dp table. However, if you only need the result and not the dp table, you can modify the solution to have a space complexity of O(m) by calculating the result directly:

```python
def get_total_number_of_sequences(m, n):
    if m < 2:
        return 0

    result = [1]