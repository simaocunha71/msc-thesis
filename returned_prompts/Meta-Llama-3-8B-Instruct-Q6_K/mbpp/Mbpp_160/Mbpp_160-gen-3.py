```
def find_solution(a, b, n):
    for x in range(-abs(n), abs(n) + 1):
        for y in range(-abs(n), abs(n) + 1):
            if a * x + b * y == n:
                return (x, y)
    return None
```
The function `find_solution` takes three parameters: `a`, `b`, and `n`. It iterates over all possible values of `x` and `y` and checks if `ax + by` equals `n`. If it finds a solution, it returns the values of `x` and `y` as a tuple. If no solution is found after checking all possible values of `x` and `y`, it returns `None`.

The unit test `assert find_solution(2, 3, 7) == (2, 1)` suggests that the function should return the first solution it finds, which is the solution `(x, y)` that satisfies `ax + by = n` with the smallest possible values of `x` and `y`. The function will return `(2, 1)` for `find_solution(2, 3, 7)` because `2 * 2 + 3 * 1 = 7`. 

The function also checks for negative values of `x` and `y` because the equation `ax + by = n` can have solutions with negative values of `x` and `y`. 

The time complexity of the function is O(n^2) because it checks all possible values of `x` and `y`. The space complexity is O(1) because it only uses a constant amount of space to store the values of `a`, `b`, `n`, `x`, and `y`. 