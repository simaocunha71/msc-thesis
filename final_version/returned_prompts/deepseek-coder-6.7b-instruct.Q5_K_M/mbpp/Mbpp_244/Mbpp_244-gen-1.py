
def next_Perfect_Square(n):
    import math
    root = math.sqrt(n)
    if root != int(root):
        root = int(root) + 1
    return root * root

assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(121) == 144
assert next_Perfect_Square(80) == 81
assert next_Perfect_Square(99) == 121
assert next_Perfect_Square(111) == 121
assert next_Perfect_Square(289) == 324
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
