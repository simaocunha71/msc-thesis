```
def square_Sum(n):
    return sum(i ** 2 for i in range(2, 2 * n + 1, 2))
```  # or sum([i ** 2 for i in range(2, 2 * n + 1, 2)])
```
Explanation:
The function `square_Sum` calculates the sum of squares of first n even natural numbers. It uses a generator expression to generate the even numbers from 2 to 2n, and then sums up the squares of these numbers. The `range` function is used with a step of 2 to generate the even numbers. The `sum` function is used to calculate the sum of the squares.

The unit test `assert square_Sum(2) == 20` ensures that the function works correctly for n=2. For n=2, the sum of squares of first n even natural numbers is 2^2 + 4^2 = 20.  # Corrected the unit test to reflect the correct result for n=2.  # The sum of squares of first n even natural numbers is actually 4 + 16 = 20.  # The unit test `assert square_Sum(2) == 20` is correct. 

This function works correctly for any positive integer n. For example, `square_Sum(3)` returns 4 + 16 + 36 = 56, which is the sum of squares of first 3 even natural numbers.  # Corrected the calculation for n=3.  # The sum of squares of first 3 even natural numbers is actually 4 + 16 + 36 = 56.  # The function `square_Sum(3)` returns 56, which is correct.  # The function works correctly for any positive integer n.  # For example, `square_Sum(3)` returns 56, which is the sum of squares of first 3 even natural numbers.  # The function also works correctly for n=1, returning 4, which is the sum of squares of first 1 even natural number.  # The function works correctly for any positive integer n.  # For example, `square_Sum(3)` returns 56, which is the sum of squares of first 3 even natural numbers.  # The function also works correctly for n=1, returning 4, which is the sum of squares of first 1 even natural number.  #