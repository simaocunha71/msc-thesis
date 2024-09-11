def last_Digit_Factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n==3):
        return 6
    if(n==4):
        return 4
    else:
        x=last_Digit_Factorial(n-1)
        y=last_Digit_Factorial(n-2)
        z=last_Digit_Factorial(n-3)
        return (x%10)*(y%10)*(z%10)%10


# Driver code
print(last_Digit_Factorial(4))
"""
Explanation:
The problem is to write a function that finds the last digit in the factorial of a given number.

Here is a function that does that:

def last_Digit_Factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(n==3):
        return 6
    if(n==4):
        return 4
    else:
        x=last_Digit_Factorial(n-1)
        y=last_Digit_Factorial(n-2)
        z=last_Digit_Factorial(n-3)
        return (x%10)*(y%10)*(z%10)%10

This function uses recursion to calculate the factorial of a given number. It starts by checking if the number is 0, 1, 2, or 3, and returns the corresponding factorial value. If the number is 4, it returns 4. If the number is greater than 4, it recursively calls itself with the previous three numbers, and then multiplies the results together modulo 10. This is done to find the last digit of the factorial.

To verify that the function works correctly, we can use the assert statement to check if the function returns the correct result for the given input. In this case, we assert that last_Digit_Factorial