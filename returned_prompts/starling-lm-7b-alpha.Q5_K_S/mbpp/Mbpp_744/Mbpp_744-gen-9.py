"""
def check_none(t):
    for x in t:
        if x is None:
            return True
    return False
"""

# Python3 Program to check if a tuple has None
def check_none(t):
    for x in t:
        if x is None:
            return True
    return False

# Driver program
print(check_none((10, 4, 5, 6, None)))  # True
print(check_none((10, 4, 5, 6)))  # False

# This code is contributed by Ankit Raj(coding_ninja)
```
```