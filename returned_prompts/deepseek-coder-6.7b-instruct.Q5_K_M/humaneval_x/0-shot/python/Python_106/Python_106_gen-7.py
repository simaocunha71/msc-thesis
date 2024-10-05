
def f(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x-1)

    def sum_of_numbers(x):
        return (x * (x + 1)) // 2

    result = []

    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_of_numbers(i))

    return result


print(f(5))  # [1, 2, 6, 24, 15]

```

This python program defines two helper functions `factorial` and `sum_of_numbers` to calculate the factorial of a number and the sum of numbers from 1 to a number respectively. The main function `f` creates a list `result` of size `n`. For each `i` from 1 to `n`, it checks whether `i` is even. If `i` is even, it appends the factorial of `i` to `result`. Otherwise, it appends the sum of numbers from 1 to `i` to `result`. Finally, it returns `result`.

This program uses recursion to calculate the factorial of a number. The base case is when `x` is 0, in which case it returns 1. Otherwise, it returns `x` multiplied by the factorial of `x-1`.

The function `sum_of_numbers` calculates the sum of numbers from 1 to `x` using the formula `(x * (x + 1)) // 2`.

In the example `f(5)`, the list `result` is `[1, 2, 6, 24, 15]`, which are the factorials of the even indices and the sums of numbers from 1 to the odd indices respectively.
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
