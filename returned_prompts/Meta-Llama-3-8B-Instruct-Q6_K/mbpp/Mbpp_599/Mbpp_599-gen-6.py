```
def sum_average(n):
    total_sum = sum(range(1, n + 1))
    average = total_sum / n
    return total_sum, average
```


The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function correctly calculates the sum and average of the first 10 natural numbers. The function uses the built-in `sum` function and the `range` function to calculate the sum of the first n natural numbers, and then calculates the average by dividing the sum by n. The function returns a tuple containing the sum and the average. 





