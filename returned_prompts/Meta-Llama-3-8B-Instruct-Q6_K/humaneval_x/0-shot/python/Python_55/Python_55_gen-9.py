```
def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This solution works by recursively calling the function with decreasing values of `n` until it reaches the base case of `n <= 1`. The base case is handled by returning the value of `n` directly. For larger values of `n`, the function combines the results of the two recursive calls by adding the `n-1`th and `n-2`th Fibonacci numbers.

However, this solution is inefficient and can lead to a stack overflow for large values of `n` due to the excessive recursion. A more efficient solution would be to use an iterative approach or memoization to store the results of previously computed Fibonacci numbers. Here's an example of a memoized solution:
```
def fib(n: int, memo={}):
    if n <= 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
```
This solution uses a dictionary `memo` to store the results of previously computed Fibonacci numbers. Before computing a new Fibonacci number, it checks if the result is already stored in the dictionary. If it is, it returns the stored result instead of recomputing it. This approach avoids the need for excessive recursion and makes the function more efficient.