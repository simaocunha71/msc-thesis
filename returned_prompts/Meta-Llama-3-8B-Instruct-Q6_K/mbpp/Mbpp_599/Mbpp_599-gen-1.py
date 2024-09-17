```
def sum_average(n):
    sum_of_natural_numbers = n*(n+1)//2
    average = sum_of_natural_numbers/n
    return sum_of_natural_numbers, average
```
Explanation:
The function `sum_average` takes an integer `n` as input and calculates the sum and average of the first `n` natural numbers.

The sum of the first `n` natural numbers is calculated using the formula `n*(n+1)//2`.

The average is calculated by dividing the sum by `n`.

The function returns a tuple containing the sum and average of the first `n` natural numbers.

The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function is working correctly. For example, the sum of the first 10 natural numbers is 55, and the average is 5.5.