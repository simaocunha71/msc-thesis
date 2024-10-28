```
def find_solution(a, b, n):
    for x in range(n + 1):
        for y in range(n + 1):
            if a * x + b * y == n:
                return (x, y)
    return None
```


This function uses a brute-force approach to find the solution. It iterates over all possible values of x and y, and checks if the equation ax + by = n is satisfied. If it finds a solution, it returns the tuple (x, y). If it doesn't find a solution after checking all possible values, it returns None.

The unit test `assert find_solution(2, 3, 7) == (2, 1)` suggests that the function should return the first solution it finds, which is (2, 1) for the equation 2x + 3y = 7. If the function finds multiple solutions, it will return the first one it finds.

Note that this function has a time complexity of O(n^2), which may not be efficient for large values of n. A more efficient approach would be to use the Extended Euclidean Algorithm to find the solution, but that would require more complex code.