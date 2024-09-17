
def number_ctr(s):
    return sum(c.isdigit() for c in s)
"""
The function `number_ctr` takes a string `s` as input. It returns the sum of the results of the `isdigit` method applied to each character in `s`. The `isdigit` method returns `True` if the character is a digit and `False` otherwise. The sum of these results gives the total number of digits in `s`.
"""

