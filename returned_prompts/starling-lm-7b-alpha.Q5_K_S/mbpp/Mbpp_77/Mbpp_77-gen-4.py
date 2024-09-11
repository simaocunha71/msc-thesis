"""
Here is the Python function to check whether a number is divisible by 11 or not.

The function works by subtracting the last digit from the first digit, then subtracting the last but one digit from the second digit, and continuing this process till the penultimate digit is reached. If the result is zero, the number is divisible by 11.

"""

def is_Diff(n):
    d = n % 11
    if d == 0:
        return True
    else:
        return False

# Testing the function
assert is_Diff(12345) == False

"""
The above function can be tested with the following code:

is_Diff(12345) == False
"""

# Another approach is to use the modulus of the sum and difference of the digits:

def is_Divisible(n):
    sum_digits = sum(map(int, str(n)))
    return (sum_digits % 11 == 0) or ((n - sum_digits) % 11 == 0)

# Testing the function
assert is_Divisible(12345) == False

"""
The above function can be tested with the following code:

is_Divisible(12345) == False
"""

# Yet another approach is to use the modulus of the sum of the digits:

def is_Divisible(n):
    sum_digits = sum(map(int, str(n)))
    return sum_digits % 11 == 0

# Testing the function
assert is_Divisible(12345) == False

"""
The above function can be tested with the following code:

is_Divisible(12345) == False
"""

# Yet another approach is to use the modulus of the difference of the digits:

def is_Divisible(n):
    diff_digits = abs(sum(map(int, str(n))) - 2 * int(str(n)[-1]))
    return diff_digits % 11 == 0

# Testing the function
assert is_