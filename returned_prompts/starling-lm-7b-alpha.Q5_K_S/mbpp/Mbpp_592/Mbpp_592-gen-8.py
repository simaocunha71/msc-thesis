def sum_Of_product(n):
    # calculate binomial coefficient
    def binomial(n, r):
        if r == 0:
            return 1
        else:
            return n * binomial(n-1, r-1) / r
    # calculate sum of product
    summ = 0
    for i in range(n+1):
        summ += binomial(n, i) * binomial(n-1, i)
    return summ

# unit tests
assert sum_Of_product(3) == 15
print("All unit tests passed.")







"""
In the problem, we are asked to find the sum of the product of consecutive binomial coefficients. To solve this problem, we can use the following steps:

1. Define a function called binomial that takes two parameters: n and r. This function calculates the binomial coefficient of n choose r using the formula: n * binomial(n-1, r-1) / r. If r is 0, it returns 1.

2. Define a function called sum_Of_product that takes one parameter: n. This function calculates the sum of the product of consecutive binomial coefficients using a for loop. It initializes the summ variable to 0 and then iterates through a range from 0 to n+1. In each iteration, it adds the product of binomial(n, i) and binomial(n-1, i) to the summ variable.

3. Finally, the sum_Of_product function returns the summ variable, which is the sum of the product of consecutive binomial coefficients.

To validate the solution, a unit test is included to check if the sum_Of_product function correctly calculates the sum of the product of consecutive binomial coefficients for the input 3, which should equal 15.

The output of the program is "All unit tests passed." if the unit test passes, indicating that the solution is correct.
"""
















































