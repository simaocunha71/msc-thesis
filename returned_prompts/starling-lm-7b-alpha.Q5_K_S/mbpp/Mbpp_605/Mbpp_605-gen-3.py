"""
def prime_num(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
"""

def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


assert prime_num(13)==True
assert prime_num(15)==False
assert prime_num(1)==False
assert prime_num(2)==True
assert prime_num(4)==False


"""
The function prime_num checks whether the given integer is a prime number. Here are some details about the function:

The function returns True if the given integer is a prime number, and False otherwise.

The function first checks if the given integer is less than 2. If it is, the function returns False, as numbers less than 2 are not prime.

Next, the function uses a for loop to iterate from 2 to the given integer (exclusive). For each iteration, the function checks if the given integer is divisible by the current iteration value (i). If it is, the function immediately returns False, as this means the given integer is not a prime number.

If the function completes the for loop without finding a divisor for the given integer, it means the given integer is a prime number. In this case, the function returns True.
"""


def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


assert prime_num(13)==True
assert prime_num(15)==False
assert prime_num(1)==False
assert prime_num(2)==True
assert prime_num(4)==False


"""
The function prime_num checks whether the given integer is a prime number. Here are some details about the function:

The function returns True if the given integer is a prime number,