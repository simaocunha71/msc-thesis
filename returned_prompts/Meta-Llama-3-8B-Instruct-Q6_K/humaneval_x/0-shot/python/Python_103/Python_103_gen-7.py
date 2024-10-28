```
def rounded_avg(n, m):
    if n > m:
        return -1
    total = sum(range(n, m+1))
    avg = round(total / (m - n + 1))
    return bin(avg)[2:]
```



Explanation:
- The function `rounded_avg(n, m)` takes two positive integers `n` and `m` as input.
- It first checks if `n` is greater than `m`, in which case it returns `-1` as per the problem statement.
- If `n` is not greater than `m`, it calculates the sum of the integers from `n` to `m` (inclusive) using the `sum` function and a generator expression.
- It then calculates the average by dividing the sum by the number of integers (which is `m - n + 1`).
- The average is rounded to the nearest integer using the `round` function.
- The binary representation of the rounded average is obtained by converting the integer to a binary string using the `bin` function, and then slicing the resulting string to remove the '0b' prefix.
- The final result is returned as a string.