```
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = (n*(n+1))//2
    return sum_of_cubes - sum_of_numbers
```


The problem is asking to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers. 

The unit test `assert difference(3) == 30` suggests that the function should take an integer as input and return the difference. 

The sum of cubes of the first n natural numbers is given by the formula: 1^3 + 2^3 + 3^3 + ... + n^3. This can be calculated using the `sum` function and a generator expression.

The sum of the first n natural numbers is given by the formula: 1 + 2 + 3 + ... + n. This can be calculated using the formula `n*(n+1)//2`.

Here is the Python function that implements this:

```
def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = (n*(n+1))//2
    return sum_of_cubes - sum_of_numbers
```


This function first calculates the sum of cubes of the first n natural numbers using a generator expression and the `sum` function. Then it calculates the sum of the first n natural numbers using the formula `n*(n+1)//2`. Finally, it returns the difference between these two sums.