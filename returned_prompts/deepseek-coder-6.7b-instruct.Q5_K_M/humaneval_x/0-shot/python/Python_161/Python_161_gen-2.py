
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)

print(solve("1234"))  # 4321
print(solve("ab"))  # AB
print(solve("#a@C"))  # "#A@c"
print(solve("1234ab"))  # "4321AB"
print(solve("ab1234"))  # "AB1234"
print(solve("1234"))  # "4321"
print(solve(""))  # ""

This program first checks if there is any letter in the string. If not, it reverses the string. If there is, it iterates over the string, and for every character, if it's lower case, it makes it upper case and vice versa.

It returns the resulting string.
"""

# ---------------------------------------------
# Solution 2
# ---------------------------------------------

"""
