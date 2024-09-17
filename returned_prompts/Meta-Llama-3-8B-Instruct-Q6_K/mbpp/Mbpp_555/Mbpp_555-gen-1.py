The problem is asking to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. 

The sum of cubes of the first n natural numbers can be calculated using a formula: sum(i^3 for i in range(1, n+1)). The sum of the first n natural numbers can be calculated using a formula: n*(n+1)/2.

Here is the Python function that solves the problem:
```
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_natural_numbers = n*(n+1)//2
    return sum_of_cubes - sum_of_natural_numbers
```
This function uses the formula for the sum of cubes and the sum of natural numbers to calculate the difference. The unit test `assert difference(3) == 30` ensures that the function is working correctly. 