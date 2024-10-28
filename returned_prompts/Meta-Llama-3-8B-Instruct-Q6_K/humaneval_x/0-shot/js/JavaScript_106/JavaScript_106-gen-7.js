Here is a Python implementation of the function `f` as described:
```
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i-1)
```
Here's an explanation of how the function works:
1. The function `f` takes an integer `n` as input and initializes an empty list `result`.
2. It iterates over the range `1` to `n+1` (inclusive) using a for loop.
3. For each `i` in the range, it checks if `i` is even by using the modulo operator `%`. If `i` is even, it calculates the factorial of `i` using the recursive function `factorial` and appends it to the `result` list.
4. If `i` is odd, it calculates the sum of numbers from `1` to `i` using the `sum` function and the `range` function, and appends it to the `result` list.
5. Finally, the function returns the `result` list.

The `factorial` function is a recursive function that calculates the factorial of a given integer `i`. It returns `1` if `i` is `0`, and otherwise returns the product of `i` and the factorial of `i-1`.

You can test the function with the example input `f(5)` to get the output `[1, 2, 6, 24, 15]`.