
def simplify(x, n):
    num1, den1 = map(int, x.split("/"))
    num2, den2 = map(int, n.split("/"))

    return (num1 * num2) % (den1 * den2) == 0

# Test cases
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False

This solution works by first splitting the input strings into numerators and denominators. It then calculates the result of the multiplication operation using the given numerators and denominators, and checks if the result is a whole number by checking if the remainder when divided by 1 is 0. If the remainder is 0, the function returns True; otherwise, it returns False.

Note: This solution assumes that the input strings are always valid fractions. If there's a chance that they might not be valid, you should add error checking to handle those cases.
"""

# 