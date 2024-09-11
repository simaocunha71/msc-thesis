def is_Even(n):
    if (n%2 == 0):
        return True
    else:
        return False

# Testing the function
print(is_Even(1))



"""
Explanation:
The function checks if a given number is divisible by 2. If it is divisible by 2, it means that the number is even.
In the function is_Even(), the modulus operator (%) is used to check if the number n is divisible by 2.
If the remainder of the division of n by 2 is 0, the function returns True, indicating that the number is even.
If the remainder is not 0, the function returns False, indicating that the number is not even.
"""




"""
In the provided code, the function is_Even() takes an argument n and checks if it's even or not. It uses the modulus operator (%) to check if n is divisible by 2. If the remainder of the division of n by 2 is 0, it means that n is even and the function returns True. If the remainder is not 0, it means that n is not even and the function returns False.

To test the function, the assert statement is used to compare the result of is_Even(1) with False. Since 1 is not divisible by 2, the function should return False, which is expected by the assert statement.

Finally, the function is_Even(1) is called and the result is printed, which should be False.
"""


"""
The assert statement is used to check if a condition is true. If the condition is false, the program will raise an AssertionError. In the provided code, the assert statement is used to check if is_Even(1) is equal to False. Since is_Even(1) should return False, the assert statement should not raise an error.
"""


"""
The function is_Even() takes an argument n and checks if it's even or not. It uses the modulus operator (%) to check if n is divisible by 2. If the remainder of the division of n by 2 is 0, it means that n is even and the function returns True. If the remainder is not 0, it means that n is not even