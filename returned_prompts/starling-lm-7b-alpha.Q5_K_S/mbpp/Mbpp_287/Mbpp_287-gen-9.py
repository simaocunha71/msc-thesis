def square_Sum(n):
    if n == 1:
        return 4
    else:
        return (n*n+square_Sum(n-1))

# Testing
assert square_Sum(2) == 20
print("Test Passed")




"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.

To do this, you need to define a function that takes an integer n as an input. In the function, you should check if the value of n is equal to 1. If it is, you should return 4, which is the square of the first even number. If the value of n is not equal to 1, you should use recursion to calculate the square of the number n and add it to the result of the function called with the argument n-1. This will continue until the base case of n equal to 1 is reached.

Once the function is defined, you can test it by calling it with the argument 2 and checking if the result is equal to 20. If the result is equal to 20, the test will pass and the function will be considered correct. Otherwise, the test will fail.

The function will return the correct result if the test passes, and this indicates that the function is working correctly.
"""

"""
Explanation:

To solve this problem, we can use the concept of recursion. Recursion is a technique in which a function calls itself in order to solve a problem. In this case, we define a function called square_Sum that takes an integer n as an input.

Inside the function, we first check if the value of n is equal to 1. If it is, we return 4, which is the square of the first even number. If the value of n is not equal to 1, we use recursion to calculate the square of the number n and add it to the result of the function called with the argument n-1. This process continues until the base case of n equal to 1 is reached.

After defining the function, we can test it by calling it with the argument 2 and checking if the result is equal to 20. If the result is equal to 20, the test will pass and we can conclude that the function is