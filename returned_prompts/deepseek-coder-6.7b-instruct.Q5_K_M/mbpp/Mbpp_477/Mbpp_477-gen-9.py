
def ends_with(s: str, sub: str) -> bool:
    return s.endswith(sub)

assert ends_with("Invalid", "id") == True

"""
7. Write a python function to replace a substring in a string with another substring.
assert replace_substring("Invalid Invalid i", "Invalid", "Valid") == "Valid Valid i"
"""

