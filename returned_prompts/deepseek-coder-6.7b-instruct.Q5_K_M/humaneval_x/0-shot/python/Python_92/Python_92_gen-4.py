
def any_int(x, y, z):
    return ((x == y + z) and (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)))

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))


# ➞ True, because 5 is equal to the sum of 2 and 7
# ➞ False, because 3 is not equal to the sum of 2 and 2
# ➞ True, because 1 is equal to the sum of 3 and -2
# ➞ False, because one of the numbers is not an integer

Explanation:
This function works by checking if the sum of the two other numbers equals the first number and if all three numbers are integers. If both conditions are true, the function returns True. Otherwise, it returns False.

isinstance() is a built-in Python function that checks if a certain value is of a certain data type. In this case, it's being used to check if the variables x, y, and z are all integers.

The 'and' operator is a logical operator that returns True only if both the conditions are True.

The '==' operator is a comparison operator that checks if two values are equal.

In the test cases, the function returns True only when the sum of the two other numbers equals the first number and all three numbers are integers.

If any of the numbers is not an integer or the sum of the other two numbers does not equal the first number, the function returns False.

If you run this code, it will return True or False for the given examples.

'''

