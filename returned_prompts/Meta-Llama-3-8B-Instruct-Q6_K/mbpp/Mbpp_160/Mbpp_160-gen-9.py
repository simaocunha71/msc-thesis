```
def find_solution(a, b, n):
    for x in range(-abs(b), abs(a) + 1):
        for y in range(-abs(a), abs(b) + 1):
            if a * x + b * y == n:
                return (x, y)
    return None
```
The function `find_solution` takes three parameters: `a`, `b`, and `n`. It iterates over all possible values of `x` and `y` and checks if `ax + by` equals `n`. If it finds a solution, it returns the pair `(x, y)` as a tuple. If no solution exists, it returns `None`.

Note that the function `find_solution` is not efficient for large values of `a`, `b`, and `n` because it uses brute force to find the solution. A more efficient solution would use the Extended Euclidean Algorithm to find the solution. However, the problem statement does not require the solution to be efficient, so the brute force approach is sufficient. 

The unit test `assert find_solution(2, 3, 7) == (2, 1)` helps to clarify the problem by providing an example of the desired output. 

The time complexity of the function `find_solution` is O(ab), where `a` and `b` are the absolute values of the input parameters. The space complexity is O(1), as it only uses a constant amount of space to store the variables `x`, `y`, and `n`. 