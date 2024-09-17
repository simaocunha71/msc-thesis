The problem is asking to find the size of the largest subset of a list of numbers such that every pair of numbers in the subset is divisible. 

The unit test `assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4` suggests that the numbers in the list are integers. 

We can solve this problem by sorting the list and then iterating through the list to find the largest subset. We can use a dynamic programming approach to keep track of the size of the largest subset ending at each position.

Here is the Python solution:

```python
def largest_subset(numbers):
    numbers.sort()
    dp = [1] * len(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] % numbers[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

This function first sorts the list of numbers. Then it initializes a dynamic programming array `dp` with all elements set to 1. This is because the largest subset ending at each position is at least of size 1 (the number itself).

The function then iterates through the list, and for each number, it checks all previous numbers to see if the current number is divisible by the previous number. If it is, it updates the `dp` array with the maximum size of the subset ending at the current position.

Finally, the function returns the maximum size of the subset found in the `dp` array. This is the size of the largest subset of numbers such that every pair is divisible. 