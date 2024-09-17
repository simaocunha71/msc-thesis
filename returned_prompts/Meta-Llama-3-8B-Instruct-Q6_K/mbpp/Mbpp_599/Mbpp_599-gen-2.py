```
def sum_average(n):
    sum = n * (n + 1) // 2
    average = sum / n
    return sum, average
```


The function `sum_average(n)` takes an integer `n` as input and returns a tuple containing the sum and average of the first `n` natural numbers.

The sum of the first `n` natural numbers is given by the formula `n * (n + 1) / 2`. This is calculated using integer division `//` to ensure the result is an integer.

The average is calculated by dividing the sum by `n`.

The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function returns the correct sum and average for the first 10 natural numbers.