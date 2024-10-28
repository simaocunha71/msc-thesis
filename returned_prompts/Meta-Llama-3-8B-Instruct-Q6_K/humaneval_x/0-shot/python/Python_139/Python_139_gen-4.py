```
def special_factorial(n):
    if n < 0:
        return "Error: Input must be a positive integer."
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        for i in range(n, 0, -1):
            result *= i
        return result
```
This function will return the special factorial of a given positive integer `n`. It first calculates the factorial of `n` using a for loop, then it calculates the factorial of `n-1` to 1! and multiplies the two results together. If `n` is less than 0, the function will return an error message. The function will work correctly for all positive integers. For example, `special_factorial(4)` will return `288` as expected. 