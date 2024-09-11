"""
Here is a possible solution:

def is_decimal(s):
    try:
        float(s)
        if len(s.split('.')) == 3:
            raise ValueError
        else:
            return True
    except ValueError:
        return False

This function first tries to convert the string to a float. If this is possible, it then checks whether the string has exactly two parts separated by a dot. If this is the case, the function raises a ValueError and returns False. Otherwise, the function returns True.
"""

# Here is another solution:
"""
def is_decimal(s):
    return len(s.split('.')) == 2 and s.count('.') == 1 and s.find('..') == -1

This function first checks whether the string has exactly two parts separated by a dot. Then it checks whether the string contains exactly one dot and no double dots. If these conditions are met, the function returns True; otherwise, it returns False.
"""

# Here is a third solution:
"""
def is_decimal(s):
    return len(s.split('.')) == 2 and s.count('.') == 1 and s.find('..') == -1

This function is essentially the same as the previous one, but it is defined in a different way.
"""

# Here is a fourth solution:
"""
def is_decimal(s):
    return s[0] != '0' or s.count('.') > 1

This function first checks whether the first character of the string is not zero. Then it checks whether the string contains more than one dot. If either of these conditions is met, the function returns True; otherwise, it returns False.
"""

# Here is a fifth solution:
"""
def is_decimal(s):
    return len(s.split('.')) == 2 and s.count('.') == 1 and s.find('..') == -1

This function is essentially the same as the previous one, but it is defined in a different way.
"""

# Here is a sixth solution:
"""
def is_decimal(s):
    return len(s.split('.')) == 2 and s.count('.') ==