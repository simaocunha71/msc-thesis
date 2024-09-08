def opposite_Signs(num1,num2):
    return (num1 ^ num2) < 0

print(opposite_Signs(1,-2)) # returns True

"""
Explanation:
The function takes two integers as input. It uses the bitwise XOR operator (^) to determine if the two numbers have the same sign (the XOR of both numbers would be positive if they have the same sign). If the XOR is negative (which means the two numbers have opposite signs), the function returns True. If not, it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Q2:
<jupyter_code>
