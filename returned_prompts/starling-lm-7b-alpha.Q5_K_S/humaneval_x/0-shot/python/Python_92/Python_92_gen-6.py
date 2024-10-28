
def any_int(x, y, z):
    # Checking if all the numbers are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    # Checking if one of the numbers is equal to the sum of the other two
    else:
        return (x == y + z or y == x + z or z == x + y)

# Testing the function
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False














```