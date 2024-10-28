```
def find_solution(a, b, n):
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            if a*x + b*y == n:
                return (x, y)
    return None
```


The unit test `assert find_solution(2, 3, 7) == (2, 1)` suggests that the function should return the first solution it finds. Therefore, we can use a brute force approach to iterate over all possible values of x and y, and return the first pair that satisfies the equation ax + by = n.

If no solution is found after checking all possible values, the function returns None. Note that this approach may not be efficient for large values of a, b, and n, as it has a time complexity of O(n^2). For larger values, more efficient algorithms such as the Extended Euclidean Algorithm can be used to find the solution. 





This is a solution in Python. The function takes three parameters: `a`, `b`, and `n`. It then iterates over all possible values of `x` and `y` in the range `-n` to `n` (inclusive), and checks if `ax + by` equals `n`. If it finds a solution, it returns the pair `(x, y)`. If it doesn't find a solution after checking all possible values, it returns `None`. 

The unit test `assert find_solution(2, 3, 7) == (2, 1)` suggests that the function should return the first solution it finds, so we don't need to worry about finding all solutions. 

Note that this solution is not efficient for large values of `a`, `b`, and `n`, as it has a time complexity of O(n^2). For larger values, more efficient algorithms such as the Extended Euclidean Algorithm can be used to find the solution.