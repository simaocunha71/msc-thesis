Here is the python code that solves the problem:

```python
def find_Average_Of_Cube(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    avg = sum_of_cubes/n
    return avg
```

This function works by first creating a list of cubes of the first n natural numbers using list comprehension. Then it calculates the sum of these cubes and divides it by n to find the average.

In this problem, n is guaranteed to be greater than 0, so there is no need for error checking.
"""

