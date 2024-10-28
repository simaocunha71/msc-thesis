The problem asks to create a function that calculates the sum of the squares of the first n odd natural numbers. 

However, the problem does not specify whether the sequence starts from 1 or 3. 

Thanks to the unit test `assert square_Sum(2) == 10`, we can assume that the sequence starts from 1, and the sum of the squares of the first n odd natural numbers is the sum of the squares of 1, 3, 5, ..., 2n-1.

Here is the Python function that solves the problem:

```python
def square_Sum(n):
    total_sum = 0
    for i in range(1, 2*n, 2):
        total_sum += i ** 2
    return total_sum
```

This function uses a for loop to iterate over the first n odd natural numbers, squares each number, and adds it to the total sum. The `range(1, 2*n, 2)` generates a sequence of odd numbers starting from 1 and ending at 2n-1. The function then returns the total sum. 

For example, if we call `square_Sum(2)`, it will return the sum of the squares of the first 2 odd natural numbers, which is 1^2 + 3^2 = 10. 