```
def cube_Sum(n):
    return sum(i**3 for i in range(2, 2*n+2, 2))
```
The function `cube_Sum(n)` calculates the sum of the cubes of the first `n` even natural numbers. It uses a generator expression inside the `sum` function to calculate the sum. The `range` function is used to generate the sequence of even numbers, starting from `2`, and ending at `2*n+2` (because the last even number is `2*n`, not `2*n+1`). The `range` function is incremented by `2` each time to generate the next even number. The function returns the sum of the cubes of these even numbers. 

The unit test `assert cube_Sum(2) == 72` ensures that the function is working correctly. 

For example, if `n` is `2`, the function should return the sum of the cubes of the first `2` even natural numbers, which are `2` and `4`. The sum of their cubes is `2^3 + 4^3 = 8 + 64 = 72`. 

The time complexity of this function is O(n), where `n` is the input. The space complexity is O(1), as it only uses a constant amount of space to store the variables. 