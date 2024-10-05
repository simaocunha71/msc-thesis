Here is a Python implementation of the `fib4` function using a loop:
```
def fib4(n):
    if n <= 1:
        return 0
    if n == 2:
        return 2
    a, b, c, d = 0, 0, 2, 0
    for i in range(3, n+1):
        temp = a + b + c + d
        a, b, c, d = b, c, d, temp
    return d
```
This function is similar to the JavaScript implementation, but uses Python's syntax and semantics. The time complexity of this function is also O(n), which is much faster than a recursive implementation.

You can test this function using the examples you provided:
```
print