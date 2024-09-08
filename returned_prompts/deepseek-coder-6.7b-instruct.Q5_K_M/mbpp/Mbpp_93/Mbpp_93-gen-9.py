def power(a, b):
    return a ** b

assert power(3, 4) == 81

# 2nd Solution
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

assert power(3, 4) == 81

# 3rd Solution
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

assert power(3, 4) == 81

# 4th Solution
def power(a, b):
    return eval(f'{a}**{b}')

assert power(3, 4) == 81

# 5th Solution
def power(a, b):
    return pow(a, b)

assert power(3, 4) == 81
"""
"""

# 6th Solution
def power(a, b):
    return a << b if b > 0 else 1 // (a << -b)

assert power(2, 3) == 8
assert power(2, -3) == 1/8

# 7th Solution
def power(a, b):
    return math.pow(a, b)

assert power(3, 4) == 81

# 8th Solution
def power(a, b):
    return a ** b

assert power(3, 4) == 81

# 9th Solution
def power(a, b):
    return pow(a, b)

assert power(3, 4) == 81

# 10th Solution
def power(a, b):
    return a * power(a, b - 1) if b else 1

assert power(3, 4) == 81
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
"""
