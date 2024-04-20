"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""
import re
def number_ctr(str):
    return sum((int)(i) for i in re.findall('\d', str))
