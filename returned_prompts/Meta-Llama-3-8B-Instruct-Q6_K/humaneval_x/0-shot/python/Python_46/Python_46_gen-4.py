The problem can be solved using dynamic programming. The idea is to store the results of the previously computed values and use them to compute the next value.

Here is a Python solution:

```
def fib4(n: int):
    if n < 4:
        return [0, 0, 2][n]
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    return fib4_values[n]
```

This function first checks if the input number `n` is less than 4. If it is, it returns the corresponding value from the list `[0, 0, 2, 0]`. If `n` is 4 or more, it initializes a list `fib4_values` with the first 4 values of the sequence and then iterates from 4 to `n` using a for loop. In each iteration, it calculates the next value by adding the last 4 values in the sequence and appends it to the list. Finally, it returns the `n`-th value in the list. This solution has a time complexity of O(n) and a space complexity of O(n).