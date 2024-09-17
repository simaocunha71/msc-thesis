The problem asks you to write a Python function that finds the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.

The unit test `assert difference(3) == 30` suggests that the function should take an integer `n` as input and return the difference.

Here's a Python function that solves the problem:

```python
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_natural_numbers = n*(n+1)//2
    return sum_of_cubes - sum_of_natural_numbers
```

This function uses list comprehension to calculate the sum of cubes of the first n natural numbers, and then calculates the sum of the first n natural numbers using the formula `n*(n+1)//2`. Finally, it returns the difference between the two sums.