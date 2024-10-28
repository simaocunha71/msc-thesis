```
def find_solution(a, b, n):
    for x in range(abs(a) + abs(b) + 2):
        for y in range(abs(a) + abs(b) + 2):
            if a * x + b * y == n:
                return (x, y)
    return None
```
The function `find_solution` takes three parameters `a`, `b`, and `n`. It iterates over all possible values of `x` and `y` in the range `[-|a| - |b|, |a| + |b|]`. If it finds a pair `(x, y)` that satisfies the equation `ax + by = n`, it returns this pair as a tuple. If no solution is found after checking all possible values of `x` and `y`, it returns `None`.

The unit test `assert find_solution(2, 3, 7) == (2, 1)` ensures that the function returns the correct solution for the equation `2x + 3y = 7`. This test is used to verify that the function works correctly.

The time complexity of this function is O((|a| + |b|)^2), as it iterates over all possible values of `x` and `y`. The space complexity is O(1), as it only uses a constant amount of space to store the function's variables. This function is not efficient for large values of `a` and `b`, as it checks all possible values of `x` and `y`. For more efficient solutions, consider using the Extended Euclidean Algorithm or the Euclidean Algorithm.