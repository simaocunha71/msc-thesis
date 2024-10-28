```
def sum_average(n):
    total_sum = sum(range(1, n+1))
    average = total_sum / n
    return total_sum, average
```


Explanation:
The function sum_average takes an integer n as input and returns a tuple containing the sum and average of the first n natural numbers.

The sum of the first n natural numbers is calculated using the formula n*(n+1)/2, which is implemented using the built-in sum function and range function.

The average is calculated by dividing the sum by n.

The function returns a tuple containing the sum and average. For example, sum_average(10) returns (55, 5.5). 

The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function is working correctly for the input 10. 

This function passes the given unit test. 