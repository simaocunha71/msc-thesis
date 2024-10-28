The Lucas sequence is a sequence of integers, where the first two numbers are 2 and 1, and every subsequent number is the sum of the previous two numbers. 

Here is a Python function to find the n'th Lucas number:

```Python
def find_lucas(n):
    if n <= 1:
        return n
    else:
        a, b = 2, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
```

This function works by initializing `a` and `b` to the first two Lucas numbers, then iterating `n-1` times to calculate the `n`th Lucas number. In each iteration, it updates `a` and `b` to the next two numbers in the sequence. Finally, it returns `b`, which is the `n`th Lucas number. 

The unit test `assert find_lucas(9) == 76` ensures that the function is working correctly. The 9th Lucas number is indeed 76. 