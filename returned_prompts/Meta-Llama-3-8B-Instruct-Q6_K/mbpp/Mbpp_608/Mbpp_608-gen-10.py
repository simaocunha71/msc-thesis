The bell number is the number of ways to partition a set of n elements. It is denoted by Bn. The first few bell numbers are 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115964.

Here is a python function to calculate the nth bell number using the recursive formula:

bell_number(n) = sum(bell_number(k) * bell_number(n-k-1) for k in range(n))

The time complexity of this function is O(2^n) because it calls itself recursively for each k from 0 to n-1.

Here is the python code:

```Python
def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum(bell_number(k) * bell_number(n-k-1) for k in range(n))
```

This function will work for small values of n, but it will be slow for large values of n because of its high time complexity. A more efficient algorithm is needed for large values of n.

We can use memoization to store the results of the function calls and reuse them instead of recomputing them. This can reduce the time complexity to O(n).

Here is the updated python code:

```Python
def bell_number(n, memo={}):
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = sum(bell_number(k, memo) * bell_number(n-k-1, memo) for k in range(n))
        memo[n] = result
        return result
```

This function will be much faster for large values of n. It will still have a high time complexity, but the constant factor will be much smaller. For example, bell_number(20) will take about 1 second with this function, but it will take several minutes with the original function.  Python's built-in memoization is used in this function to store the results of the function calls. This is done using a dictionary called memo. The function checks if the result for a given n is already in memo before computing it. If it is, the function returns the stored result instead of recomputing it. If it is not, the function computes the result, stores it in memo, and returns it. This can greatly reduce the time it takes to compute the bell number for large values of n.  For example, bell_number(20