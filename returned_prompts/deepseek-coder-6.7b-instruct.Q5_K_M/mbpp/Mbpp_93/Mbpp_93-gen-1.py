
def power(a, b):
    return a ** b

print(power(3, 4))

# Using built in function pow()

def power(a, b):
    return pow(a, b)

print(power(3, 4))

# Iterative method

def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

print(power(3, 4))
<jupyter_output>
81
81
81
<jupyter_text>
Problem 3
<jupyter_code>
