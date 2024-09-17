
def is_woodall(n):
    str_n = str(n)
    for digit in str_n:
        if int(digit) == 0 or n % int(digit) != 0:
            return False
    return True
"""
The number 383 is a Woodall number because it has no 0 in it and its each digit divides the number.
"""


