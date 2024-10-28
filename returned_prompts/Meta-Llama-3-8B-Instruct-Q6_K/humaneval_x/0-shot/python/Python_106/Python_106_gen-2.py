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
This function iterates over the range from 1 to n (inclusive), and for each number i, it checks if i is even (using the modulus operator `%`). If i is even, it calculates the factorial of i using the `math.factorial` function and appends it to the result list. If i is odd, it calculates the sum of numbers from 1 to i using the `sum` function and appends it to the result list. Finally, it returns the result list.