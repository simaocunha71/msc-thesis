def opposite_Signs(num1, num2):
    return (num1 ^ num2) < 0

print(opposite_Signs(1,-2))

"""
Explanation:
This function uses bitwise XOR (^) operator. The XOR of two integers gives a number where bits are set at those places where the corresponding bits in the two integers are opposite. If the XOR of two numbers has negative value, it means that the signs are opposite.
"""

# OR

def opposite_Signs(num1, num2):
    return (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0)

print(opposite_Signs(1,-2))

"""
Explanation:
This function directly compares the sign of both numbers. If one number is positive and other is negative, then their signs are opposite, so this function returns True. Otherwise, it returns False.
"""
<jupyter_output>
True
True
<jupyter_text>
