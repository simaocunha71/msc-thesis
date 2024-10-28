
```python
def fib4(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib = [0, 0, 2, 0]

    for i in range(4, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4])

    return fib[n]
```

Explanation:

This function uses a list to store the Fib4 sequence up to the n-th number. The first four numbers of the sequence are manually defined, and the rest are computed using the formula provided in the problem statement.

This function is efficient because it uses a loop to calculate each number in the sequence, which runs in linear time (O(n)). It also uses a constant amount of space to store the sequence, which makes it an efficient solution.

In the case where n < 2, the function returns 0, which is the first two numbers in the Fib4 sequence. If n is 2 or 3, the function returns 2 or 0, respectively, which are the third and fourth numbers in the sequence.

The time complexity of this function is O(n) because it loops through the range of n to compute each number in the sequence. The space complexity is O(n) because it uses a list to store the sequence up to the n-th number.

This function should pass all the test cases in the provided example and produce the correct results for larger inputs.
"""

# ---------------------
"""
