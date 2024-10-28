```
def sum_Of_product(n):
    sum = 0
    for i in range(n):
        for j in range(i+1, n+1):
            sum += (n choose i) * (n choose j)
    return sum
```
The function sum_Of_product(n) calculates the sum of the product of consecutive binomial co-efficients for a given integer n. It does this by iterating over all pairs of indices i and j from 0 to n-1 and adding the product of the binomial coefficients (n choose i) and (n choose j) to the sum. The unit test `assert sum_Of_product(3) == 15` suggests that the function should return 15 for n=3. 

However, the problem statement does not specify the range of the binomial coefficients. The unit test `assert sum_Of_product(3) == 15` suggests that the range is from 0 to n. 

Please note that this function may not be efficient for large values of n due to its time complexity. It can be optimized by using dynamic programming or memoization. 

Also, the binomial coefficient (n choose i) can be calculated using the formula n! / (i! * (n-i)!) where ! denotes the factorial function. This can be calculated using the math.factorial function in Python. However, this is not necessary for the given problem as the binomial coefficients are not explicitly calculated, but instead are used as a placeholder in the formula. 

Here is the modified function with the above considerations:

```
import math
def sum_Of_product(n):
    sum = 0
    for i in range(n):
        for j in range(i+1, n+1):
            sum += math.factorial(2*n) // (math.factorial(i) * math.factorial(j) * math.factorial(n-i) * math.factorial(n-j))
    return sum
```

This function calculates the sum of the product of consecutive binomial co-efficients for a given integer n. It uses the math.factorial function to calculate the factorial of a number, and then uses this to calculate the binomial coefficient. The sum is then calculated by iterating over all pairs of indices i and j from 0 to n-1 and adding the product of the binomial coefficients to the sum. The function returns the sum. 

Please note that this function may still not be efficient for large values of n due to its time complexity. It can