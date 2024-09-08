def opposite_Signs(x, y):
    if x ^ y < 0:
        return True
    else:
        return False

print(opposite_Signs(1,-2))  # True
print(opposite_Signs(2,3))  # False
print(opposite_Signs(-4,4))  # False
print(opposite_Signs(-5,-6))  # True
<jupyter_output>
True
False
False
True
<jupyter_text>
