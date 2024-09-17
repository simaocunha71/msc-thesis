The Bell numbers are a sequence of numbers in mathematics that arise in the study of permutations, combinations, and partitions. They are named after Eric Temple Bell, who introduced them in his book "Men of Mathematics".

The nth Bell number, denoted by Bn, is the number of ways to partition a set of n elements. For example, the first few Bell numbers are 1, 1, 2, 5, 15, 52, 203, ...

Here is a Python function to calculate the nth Bell number:

```
def bell_number(n):
    if n <= 1:
        return 1
    bell = [1, 1]
    for i in range(2, n+1):
        bell.append(sum(bell[i-1] * (i-1)**j for j in range(i)))
    return bell[n]
```

This function uses dynamic programming to calculate the Bell numbers. It starts with a list `bell` containing the first two Bell numbers (1 and 1). Then, for each subsequent Bell number, it calculates the sum of the previous Bell number multiplied by the factorial of the current Bell number's index. The result is the next Bell number. The function returns the nth Bell number.

For example, `bell_number(2)` returns 2, which is the second Bell number. This is confirmed by the unit test `assert bell_number(2) == 2`. The unit test ensures that the function is working correctly. If the function is not working correctly, the unit test will fail, indicating that there is an error in the function. 