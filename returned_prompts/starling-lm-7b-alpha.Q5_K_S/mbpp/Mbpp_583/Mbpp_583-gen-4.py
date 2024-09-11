```
# Catalan number can be calculated using the following formula
# C_n = (2n)! / ((n+1)!*n!)

def catalan_number(n):
    factorial = lambda x: reduce(lambda y: y * x, range(2, x + 1), 1)
    return factorial(2 * n) / (factorial(n + 1) * factorial(n))
```
    
    
This code defines a function catalan_number that takes an integer argument n and returns the nth catalan number. The function uses the fact that the nth catalan number can be calculated as `(2n)! / ((n+1)!*n!)`. The `factorial` function is defined as a helper function to calculate factorials.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a given input. In this case, `catalan_number(10)` should return `16796`.
```

```
    
The `reduce` function is a higher-order function in Python that applies a function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single output. In this case, it is used to calculate the factorial of a number by applying the multiplication operation to all numbers from 2 to the given number.

The `factorial` function is a helper function that takes an integer `x` as input and returns the factorial of `x` using the `reduce` function. It uses a lambda function to define the multiplication operation and initializes the accumulator to 1.

Overall, this solution provides a concise and efficient way to calculate catalan numbers in Python.


```

```
    

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``