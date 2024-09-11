def last_Digit_Factorial(n):
    if n == 0:
        return 1
    elif n % 10 == 0:
        return 0
    else:
        return (n * last_Digit_Factorial(n - 1)) % 10


# Driver Code
print(last_Digit_Factorial(4))



"""
The last digit of the factorial of a given number can be found by taking the factorial of that number and finding the remainder when divided by 10. Since the factorial of any number ends in 0, the last digit will be the last non-zero digit.

In this solution, we use recursion to calculate the factorial of the given number. If the number is 0, we return 1, as the factorial of 0 is defined as 1. If the last digit of the number is 0, we return 0, as the factorial of a multiple of 10 will always end in 0. Otherwise, we multiply the number by the factorial of the number minus one, and take the remainder when divided by 10. This is done recursively until the base case is reached.
"""

"""
To find the last digit of the factorial of a given number, we can use a recursive function. Here's how it works:

First, we define a function called last_Digit_Factorial that takes a single parameter, n, which is the number we want to find the factorial of.

Inside the function, we check if the number is equal to 0. If it is, we return 1, as the factorial of 0 is defined as 1.

Next, we check if the last digit of the number is 0. If it is, we return 0, as the factorial of a multiple of 10 will always end in 0.

If neither of the above conditions is true, we multiply the number by the factorial of the number minus one, and take the remainder when divided by 10. We then recursively call the function with the new value of n. This process continues until we reach the base case, where n is 0.

Finally, we return the result of the recursive call to the function.