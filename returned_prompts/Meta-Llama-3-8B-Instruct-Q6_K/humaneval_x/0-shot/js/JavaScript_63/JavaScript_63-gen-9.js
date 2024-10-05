Here is a Python solution:

```Python
def fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
```

This function uses a simple iterative approach to compute the nth element of the fibfib sequence. It keeps track of the last three elements in the sequence (a, b, c) and updates them in each iteration. This way, it only needs to keep track of the last three elements, which makes it more efficient than a recursive approach. 

Here are some tests to demonstrate the correctness of the function:

```Python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
``` 