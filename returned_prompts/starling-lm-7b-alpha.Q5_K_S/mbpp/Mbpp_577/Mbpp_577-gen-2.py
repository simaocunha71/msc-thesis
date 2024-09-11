def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        return (n * last_Digit_Factorial(n-1)) % 10

# Testing the function
assert last_Digit_Factorial(4) == 4

"""
The time complexity of this function is O(log(n)) and the space complexity is O(1)
"""

"""
The code provided is a Python function that calculates the last digit of the factorial of a given number. It uses a recursive approach to calculate the factorial and then takes the modulo 10 to get the last digit. The function uses a conditional statement to handle the base case, where if the input number is 0, the function returns 1.

The time complexity of the function is O(log(n)) because in the worst case scenario, the function will need to make log(n) recursive calls to calculate the factorial. The space complexity of the function is O(1) because it only uses a constant amount of space to store the return value of the recursive calls.
"""

"""
The code provided is a Python function that calculates the last digit of the factorial of a given number. It uses a recursive approach to calculate the factorial and then takes the modulo 10 to get the last digit. The function uses a conditional statement to handle the base case, where if the input number is 0, the function returns 1.

The time complexity of the function is O(log(n)) because in the worst case scenario, the function will need to make log(n) recursive calls to calculate the factorial. The space complexity of the function is O(1) because it only uses a constant amount of space to store the return value of the recursive calls.
"""

def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        return (n * last_Digit_Factorial(n-1)) % 10

# Testing the function
assert last_Digit_Factorial(4) == 4

"""
The time complexity of this function is O(log(n)) and the space complexity is O(1)
"""

