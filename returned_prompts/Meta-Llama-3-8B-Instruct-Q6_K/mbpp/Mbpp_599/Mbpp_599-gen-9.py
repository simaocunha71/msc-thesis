```
def sum_average(n):
    sum = n*(n+1)//2
    average = sum/n
    return sum, average
```


The problem asks to write a function that calculates the sum and average of the first n natural numbers. 

The given unit test `assert sum_average(10)==(55, 5.5)` suggests that the function should return the sum and average as a tuple.

The formula to calculate the sum of the first n natural numbers is `n*(n+1)//2`. The average can be calculated by dividing the sum by `n`. 

Here is the Python function that implements this:

```
def sum_average(n):
    sum = n*(n+1)//2
    average = sum/n
    return sum, average
```

This function takes an integer `n` as input, calculates the sum and average, and returns them as a tuple. The unit test provided ensures that the function works correctly for `n=10`. 