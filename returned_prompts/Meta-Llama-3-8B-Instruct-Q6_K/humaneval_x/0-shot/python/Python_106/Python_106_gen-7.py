```
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result
```
The function `f(n)` iterates over the range from 1 to `n` (inclusive) and for each `i`, it checks if `i` is even or not. If `i` is even, it calculates the factorial of `i` using `math.factorial(i)` and appends it to the result list. If `i` is odd, it calculates the sum of numbers from 1 to `i` using `sum(range(1, i+1))` and appends it to the result list. Finally, it returns the result list. The example you provided, `f(5) == [1, 2, 6, 24, 15]`, can be verified by running the function.