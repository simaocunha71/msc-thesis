
def any_int(x, y, z):
    if (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        if (x == y + z) or (y == x + z) or (z == x + y):
            return True
    return False

print(any_int(5, 2, 7))  # ➞ True

print(any_int(3, 2, 2))  # ➞ False

print(any_int(3, -2, 1))  # ➞ True

print(any_int(3.6, -2.2, 2))  # ➞ False

print(any_int(3, 2, 5))  # ➞ True

print(any_int(1, 0, 1))  # ➞ True

print(any_int(-1, 0, 1))  # ➞ True

print(any_int(5, 3, 2))  # ➞ False

print(any_int(1, 2, 3))  # ➞ False

'''
The function 'any_int' first checks if all the inputs are integers. If not, it immediately returns False.
Then it checks if any of the inputs is equal to the sum of the other two.
If such an input is found, it returns True, otherwise it returns False.
'''


# Test the function with provided examples and some other examples

print(any_int(5, 2, 7))  # ➞ True
print(any_int(3, 2, 2))  # ➞ False
print(any_int(3, -2, 1))  # ➞ True
print(any_int(3.6, -2.2, 2))  # ➞ False

# Test the function with some other examples

print(any_int(3, 2, 5))  # ➞ True
print(any_int(1, 0, 1))  # ➞