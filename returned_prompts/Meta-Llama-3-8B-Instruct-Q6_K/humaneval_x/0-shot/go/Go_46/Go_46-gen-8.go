The Fibonacci sequence is a classic problem in computer science, and there are many ways to solve it. Here's a solution that uses a dynamic programming approach, which is efficient and easy to understand:
```python
def Fib4(n):
    if n <= 1:
        return 0
    if n == 2:
        return 2
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    return fib4_values[n]
```
This function uses a list `fib4_values` to store the values of the Fibonacci sequence up to `n`. It initializes the list with the first four values, and then iterates from `4` to `n`, calculating each value as the sum of the previous four values. Finally, it returns the `n`-th value in the list.

Here's an explanation of the code:
* `if n <= 1: return 0`: This is a base case for the Fibonacci sequence, where the first two values are 0.
* `if n == 2: return 2`: This is another base case, where the third value is 2.
* `fib4_values = [0, 0, 2, 0]`: This initializes the list with the first four values of the Fibonacci sequence.
* `for i in range(4, n+1):`: This loop iterates from `4` to `n`, calculating each value as the sum of the previous four values.
* `fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])`: This calculates the `i`-th value as the sum of the previous four values, and appends it to the list.
* `return fib4_values[n]`: This returns the `n`-th value in the list.

This solution has a time complexity of O(n), which is efficient for large values of `n`. It also uses a constant amount of space, which is a good property for a function that needs to compute values for large `n`. 