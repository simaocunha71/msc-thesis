def sum_average(n):
    # your code here
    sum = (n*(n+1))//2
    average = sum / n
    return sum, average

# assert sum_average(10)==(55, 5.5)




```

```
def sum_average(n):
    # your code here
    sum = (n*(n+1))//2
    average = sum / n
    return sum, average
```
This function takes an input `n` and calculates the sum and average of the first `n` natural numbers. The sum is calculated using the formula `(n*(n+1))//2`, and the average is calculated by dividing the sum by `n`. The function returns a tuple containing the sum and average values.

To test the function, you can use the `assert` statement followed by the expected result. In this case, the expected result is `(55, 5.5)` when `n` is `10`. This means that the sum of the first `10` natural numbers is `55` and the average is `5.5`.

By running the code, the `assert` statement will check if the result of the `sum_average` function matches the expected result. If the result is correct, the `assert` statement will pass and no error will be raised. If the result is incorrect, an error will be raised and the program will stop execution.
```

```python
def sum_average(n):
    # your code here
    sum = (n*(n+1))//2
    average = sum / n
    return sum, average
```

In this Python code, the `sum_average` function is defined to calculate the sum and average of the first `n` natural numbers. The sum is calculated using the formula `(n*(n+1))//2`, and the average is calculated by dividing the sum by `n`. The function returns a tuple containing the sum and average values.

To test the function, an assertion statement is used to check if the result of the `sum_average` function matches the expected result. In this case, the expected result is `(55, 5.5)` when