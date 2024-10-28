    import re
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if ' ' in password:
        return False
    return True

FIX = """
Add more test cases.
"""

def find_max_consecutive_sum(numbers):
    """Write a function find_max_consecutive_sum which takes a list of integers as input and returns the maximum sum of
    any consecutive subarray of the input list.

    Example:
    >>> find_max_consecutive_sum([1, 2, 3, -2, 5])
    9
    >>> find_max_consecutive_sum([-1, -