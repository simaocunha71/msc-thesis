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
In this solution, we use a list comprehension to create a list of size n. We iterate over the range from 1 to n+1 (inclusive) using the for loop. For each iteration, we check if the current index i is even using the modulo operator `%`. If i is even, we append the factorial of i to the result list using the `math.factorial` function. If i is odd, we append the sum of numbers from 1 to i using the `sum` function and the `range` function. Finally, we return the result list.

Note: You need to import the `math` module to use the `math.factorial` function. You can do this by adding `import math` at the beginning of your code.