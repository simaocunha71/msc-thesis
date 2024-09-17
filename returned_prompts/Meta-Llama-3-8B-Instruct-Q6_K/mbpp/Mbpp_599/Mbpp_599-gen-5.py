```
def sum_average(n):
    total_sum = sum(range(1, n + 1))
    average = total_sum / n
    return total_sum, average
```


The function `sum_average` takes an integer `n` as input and calculates the sum and average of the first `n` natural numbers. It uses the built-in `sum` function to calculate the sum and then calculates the average by dividing the sum by `n`. The function returns a tuple containing the sum and average. The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function works correctly for the input `n=10`. 