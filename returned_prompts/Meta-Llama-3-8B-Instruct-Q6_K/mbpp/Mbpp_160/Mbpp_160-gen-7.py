```
def find_solution(a, b, n):
    for x in range(-10000, 10001):
        for y in range(-10000, 10001):
            if a * x + b * y == n:
                return (x, y)
    return None
```
The problem is asking you to write a function that finds two integers x and y that satisfy the equation ax + by = n. If such a solution does not exist, the function should return None.

The function uses two nested loops to iterate over all possible values of x and y in the range -10000 to 10000. For each pair of values, it checks if the equation ax + by = n is satisfied. If it finds a pair that satisfies the equation, it returns the pair as a tuple. If it does not find any such pair after checking all possible values, it returns None.

The unit test `assert find_solution(2, 3, 7) == (2, 1)` ensures that the function returns the correct solution for the equation 2x + 3y = 7. The function should return (2, 1) because 2*2 + 3*1 = 7. If the function returns None, the test will fail.