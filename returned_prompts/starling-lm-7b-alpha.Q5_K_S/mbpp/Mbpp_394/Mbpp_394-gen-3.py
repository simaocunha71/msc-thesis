"""
def check_distinct(t):
    if len(t) == len(set(t)):
        return True
    return False
"""

# Alternative solution using Python's built-in set()
def check_distinct(t):
    return len(t) == len(set(t))


# Testing the function
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
print("All tests passed")

# End program
```