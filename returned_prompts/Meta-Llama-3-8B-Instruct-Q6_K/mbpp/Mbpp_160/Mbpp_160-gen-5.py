```
def find_solution(a, b, n):
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            if a * x + b * y == n:
                return (x, y)
    return None
```


The problem asks for a function that finds two integers x and y that satisfy the equation ax + by = n. The function should return these integers as a tuple if they exist, and None if no solution exists.

The unit test `assert find_solution(2, 3, 7) == (2, 1)` suggests that the function should iterate over all possible values of x and y to find the solution.

Here is a Python solution that uses two nested loops to iterate over all possible values of x and y, and returns the solution as a tuple if found, or None if no solution exists:

```
def find_solution(a, b, n):
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            if a * x + b * y == n:
                return (x, y)
    return None
```

This function iterates over all possible values of x and y within the range -1000 to 1000, and checks if the equation ax + by = n is satisfied. If a solution is found, the function returns the solution as a tuple. If no solution is found after iterating over all possible values, the function returns None.