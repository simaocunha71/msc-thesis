```
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```
Explanation:
The function `square_Sum` takes an integer `n` as input and returns the sum of the squares of the first `n` odd natural numbers. 

The `range` function is used to generate the sequence of odd numbers starting from 1, up to `2*n` (since we need `n` odd numbers). The step size is 2, which means we increment by 2 each time.

The `sum` function is used to calculate the sum of the squares of these odd numbers. The `**` operator is used to square each number.

The unit test `assert square_Sum(2) == 10` ensures that the function works correctly for `n=2`, which should return the sum of the squares of the first 2 odd numbers (1^2 + 3^2 = 10). 