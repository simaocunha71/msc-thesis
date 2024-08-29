def find(a, b):
    return a // b

# test
assert find(10,3) == 3

# or

def find(a, b):
    return int(a / b)

# test
assert find(10,3) == 3

# or

def find(a, b):
    return int(a / b) if b != 0 else 'undefined'

# test
assert find(10,3) == 3
assert find(10,0) == 'undefined'
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
