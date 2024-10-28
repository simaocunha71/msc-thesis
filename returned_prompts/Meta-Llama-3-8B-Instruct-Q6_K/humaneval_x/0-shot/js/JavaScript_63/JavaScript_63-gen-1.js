The problem can be solved by using dynamic programming to store the previously computed values. Here's a Python solution:

```python
def fibfib(n):
    if n <= 1:
        return 0
    dp = [0, 0, 1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]
```
This function initializes a list `dp` with the first three values of the fibfib sequence. Then it iterates from 3 to `n`, calculating each value as the sum of the previous three values. Finally, it returns the `n`-th value of the sequence.

This solution has a time complexity of O(n) and a space complexity of O(n), as it needs to store the previously computed values.

You can test this function with the examples you provided:

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```  """

```python
def fibfib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c
```

This function has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the three variables.  """  """

```python
def fibfib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a+b
    return a+b
```

This function has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the two variables.  """  """

```python
def fibfib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return (lambda a, b: lambda n: a if n == 