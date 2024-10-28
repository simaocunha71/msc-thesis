```
def special_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= math.factorial(i)
    return result
```

This function uses a for loop to iterate over the range from 1 to n (inclusive), and for each iteration, it multiplies the result by the factorial of the current number. The factorial of a number is calculated using the `math.factorial` function from the math module. The function returns the final result.

For example, if you call `special_factorial(4)`, it will calculate the Brazilian factorial of 4, which is `4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288`. Therefore, the function returns `288`.