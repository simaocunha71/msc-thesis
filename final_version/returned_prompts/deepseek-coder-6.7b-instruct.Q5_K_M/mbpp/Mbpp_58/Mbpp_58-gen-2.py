def opposite_Signs(x, y):
    return (x ^ y) < 0

print(opposite_Signs(1,-2))

# ^ is bitwise XOR operator, if both numbers have same sign, XOR will return positive, otherwise negative.
# So, if XOR is negative, it means that both numbers have different signs, hence, returns True.
# If XOR is positive, it means that both numbers have same sign, hence, returns False.
<jupyter_output>
True
<jupyter_text>
Question 2:
<jupyter_code>
