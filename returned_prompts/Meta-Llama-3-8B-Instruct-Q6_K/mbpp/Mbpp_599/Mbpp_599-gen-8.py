```
def sum_average(n):
    total = sum(range(1, n+1))
    average = total / n
    return total, average
```



In this problem, we need to write a function that calculates the sum and average of the first n natural numbers. For example, if n is 10, the function should return (55, 5.5) because the sum of the first 10 natural numbers is 55 (1+2+3+4+5+6+7+8+9+10) and the average is 5.5.

We can solve this problem using the built-in sum function in Python and the range function to generate the sequence of numbers. The sum function calculates the sum of all numbers in the sequence, and we divide this sum by n to get the average.

Here is the Python code for the solution:

```
def sum_average(n):
    total = sum(range(1, n+1))
    average = total / n
    return total, average
```

This function takes an integer n as input, calculates the sum of the first n natural numbers using the sum function and the range function, and then calculates the average by dividing the sum by n. The function returns a tuple containing the sum and the average.

For example, if we call the function with n=10, it will return (55, 5.5), which is the sum and average of the first 10 natural numbers. The unit test `assert sum_average(10)==(55, 5.5)` ensures that the function works correctly.