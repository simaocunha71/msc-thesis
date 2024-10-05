
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


# Tests:

print(flip_case('Hello'))  # 'hELLO'
print(flip_case('hELLO'))  # 'Hello'
print(flip_case('PythonIsFun'))  # 'pYTHONiSfUN'
print(flip_case(''))  # ''


# Explanation:

We use a list comprehension to iterate over the string, for each character we check if it's a lowercase or uppercase character and convert it to the other case using the built-in `upper()` and `lower()` functions. The `join()` function is then used to combine the resulting characters into a single string.
"""

# 2.

"""
