```
def find_solution(a, b, n):
    if a == 0 and b == 0 and n == 0:
        return (0, 0)
    elif a == 0 and b != 0 and n % b == 0:
        return (0, n // b)
    elif a != 0 and b == 0 and n % a == 0:
        return (n // a, 0)
    else:
        d = abs(b) - abs(a)
        if d == 0:
            return (None, None)
        if d < 0:
            return (None, None)
        else:
            x = (n - b) // a
            if a >= 0 and b >= 0:
                y = (n + b) // a
            elif a <= 0 and b <= 0:
                y = (n - b) // a
            elif a <= 0 and b >= 0:
                y = (n + b) // a
            elif a >= 0 and b <= 0:
                y = (n - b) // a
            return (x, y)
```

Explanation:
The function `find_solution` takes three parameters: `a`, `b`, and `n`. It uses the extended Euclidean algorithm to find integers `x` and `y` that satisfy the equation `ax + by = n`. 

If `a` and `b` are both 0 and `n` is 0, the function returns the tuple `(0, 0)`. 

If `a` and `b` are both 0 and `n` is not 0, the function returns `None` because there is no solution. 

If `a` and `b` are both non-zero and `n` is divisible by `b`, the function returns the tuple `(0, n // b)`. 

If `a` and `b` are both non-zero and `n` is divisible by `a`, the function returns the tuple `(n // a, 0)`. 

If `a` and `b` are both non-zero and `n