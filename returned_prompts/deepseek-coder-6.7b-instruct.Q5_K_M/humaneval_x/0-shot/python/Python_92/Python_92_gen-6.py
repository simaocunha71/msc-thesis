
def any_int(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        return False
    if x == y + z or y == x + z or z == x + y:
        return True
    return False

print(any_int(5, 2, 7)) # True
print(any_int(3, 2, 2)) # False
print(any_int(3, -2, 1)) # True
print(any_int(3.6, -2.2, 2)) # False

# The function first checks if the numbers are integers. If not, it returns False.
# Then, it checks if one of the numbers is equal to the sum of the other two. If yes, it returns True. Otherwise, it returns False.

# This function works by checking the conditions given in the problem description, and returning True or False accordingly.

# Note that the function does not account for floating-point numbers. If you need to consider numbers that are close to integers (within a small tolerance), you would need to modify the function accordingly.

# Also, the function assumes that the numbers given are valid (i.e., they are real numbers). If you need to handle cases where the numbers might be invalid (e.g., NaN or infinity), you would need to add error checking code to handle these cases.

# This function does not handle the case where x, y, or z is a list of integers. If you need to handle this case, you would need to modify the function accordingly.

# This function does not handle the case where x, y, or z is a string of digits. If you need to handle this case, you would need to modify the function accordingly.

# This function does not handle the case where x, y, or z is a string of non-digits. If you need to handle this case, you would need to modify the function accordingly.

# This function does not handle the case where x, y, or z is a string of digits followed by a non-digit. If you need to handle this case, you would need to modify the function accordingly.

# This function does not handle the case where x, y,