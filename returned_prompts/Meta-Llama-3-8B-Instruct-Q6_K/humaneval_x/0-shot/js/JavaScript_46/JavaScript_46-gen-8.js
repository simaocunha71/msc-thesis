Here is a Python solution for the problem:

```
def fib4(n):
    if n < 1:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        fib4_values = [0, 0, 2, 0]
        for i in range(4, n + 1):
            fib4_values.append(fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4])
        return fib4_values[n]
```
This function first checks for the base cases (n < 1, n = 1, n = 2, n = 3). For n >= 4, it calculates the n-th element of the fib4 sequence by iterating from i = 4 to n, and for each i, it calculates the i-th element as the sum of the previous four elements. The function returns the n-th element. 

For example, `fib4(5)` returns 4, `fib4(6)` returns 8, and `fib4(7)` returns 14. 

Note that this function has a time complexity of O(n) and a space complexity of O(n), as it needs to store the previous four elements in the fib4 sequence. 

If you want to optimize the space complexity, you can use a circular buffer to store the previous four elements, which would reduce the space complexity to O(1). Here is the optimized code:

```
def fib4(n):
    if n < 1:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c
        return d
```
This function uses a circular buffer to store the previous four elements, which reduces the space complexity to O(1). The time complexity remains O(n). 





