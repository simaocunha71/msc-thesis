def opposite_Signs(num1, num2):
    return (num1 ^ num2) < 0

print(opposite_Signs(1,-2))


#The XOR operator (^) returns 1 if two bits are different, else it returns 0.
#Thus, if the signs of both numbers are different, the result of (num1 ^ num2) will be negative.
#So we check if the result is less than 0 to return True or False.

#So, if the numbers have different signs, the function will return True, otherwise False.
assert opposite_Signs(1,-2) == True
assert opposite_Signs(2,3) == False
assert opposite_Signs(-4,5) == False
assert opposite_Signs(-6,-7) == True
<jupyter_output>
True
<jupyter_text>
