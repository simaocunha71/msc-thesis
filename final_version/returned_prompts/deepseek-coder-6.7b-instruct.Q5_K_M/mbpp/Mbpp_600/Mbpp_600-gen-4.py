
def is_Even(num):
    if num % 2 == 0:
        return True
    else:
        return False

assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(0) == True
assert is_Even(-1) == False
assert is_Even(-2) == True

# Alternatively, you can use the modulo operator in a single line.

def is_Even_alt(num):
    return num % 2 == 0

assert is_Even_alt(1) == False
assert is_Even_alt(2) == True
assert is_Even_alt(0) == True
assert is_Even_alt(-1) == False
assert is_Even_alt(-2) == True
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
