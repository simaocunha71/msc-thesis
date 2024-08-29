def opposite_Signs(n1, n2):
    if (n1 ^ n2) < 0:
        return True
    else:
        return False

print(opposite_Signs(1,-2))

# Bitwise XOR operator is used here to check if the two numbers have different signs. If they have, XOR will return a number with a non-zero least significant bit, which is converted to True in boolean context. If they have the same sign, XOR will return 0, which is False in boolean context.

"""
This code uses bitwise XOR operator (^) to compare the two numbers. If the two numbers have different signs, the XOR will return a non-zero value. If they have the same sign, the XOR will return 0.

The code then uses a conditional (if-else) statement to return True if the numbers have different signs and False if they have the same sign.
"""

# Bitwise XOR operator is used here to check if the two numbers have different signs. If they have, XOR will return a number with a non-zero least significant bit, which is converted to True in boolean context. If they have the same sign, XOR will return 0, which is False in boolean context.
<jupyter_output>
<empty_output>
<jupyter_text>
