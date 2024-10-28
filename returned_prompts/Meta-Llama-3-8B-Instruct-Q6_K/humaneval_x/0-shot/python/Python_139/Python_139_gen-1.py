```
def special_factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= math.factorial(i)
    return result
```
This function calculates the special factorial of a given number `n`. It starts with a result of 1 and then multiplies it by the factorial of each number from `n` down to 1. The `math.factorial` function from the Python `math` module is used to calculate the factorial of each number. The result is then returned by the function. For example, `special_factorial(4)` would return `288`.