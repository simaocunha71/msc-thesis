The Lucas sequence is a sequence of numbers that is similar to the Fibonacci sequence, but with different initial values. The Lucas sequence is defined as L(0) = 2, L(1) = 1, and L(n) = L(n-1) + L(n-2) for n > 1.

Here is a Python function that calculates the nth Lucas number:

```
def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
```
This function works by initializing two variables a and b to the first two Lucas numbers, then iteratively calculating the next Lucas number in the sequence by adding a and b and updating a and b. The function returns the nth Lucas number. The unit test `assert find_lucas(9) == 76` ensures that the function is working correctly. 