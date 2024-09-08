def opposite_Signs(x, y):
    return (x ^ y) < 0

print(opposite_Signs(1, -2))


# ^ operator is the XOR operator in python. It returns 1 if the two compared values are different, otherwise it returns 0.
# So, when we compare x^y with 0, we get 1 if x and y have different signs and 0 if they have the same sign.
# Comparing a positive integer with -1 will always give a negative integer, hence it can be used as a condition to check if x and y have different signs.

# Note: The ^ operator is a bitwise operator and the above solution assumes that the two integers are in a 32-bit two's complement binary representation. If the integers can be larger than 32 bits, the solution would need to be adapted accordingly.
<jupyter_output>
True
<jupyter_text>
Exercise 2:
<jupyter_code>
