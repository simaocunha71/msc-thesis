```
def sum_average(n):
    total = 0
    for i in range(1, n+1):
        total += i
    average = total / n
    return total, average
```


The function `sum_average` takes an integer `n` as input and returns a tuple containing the sum and average of the first `n` natural numbers. It uses a for loop to calculate the sum and then divides the sum by `n` to calculate the average. The function passes the given unit test `assert sum_average(10) == (55, 5.5)`. 