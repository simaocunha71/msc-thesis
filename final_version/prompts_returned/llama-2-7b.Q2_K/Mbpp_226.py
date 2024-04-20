"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
import re

odd_values = [x for x in range(2,5) if x % 2 != 0] + [10]  # 9 11  13 15


def odd_values_string(s):
    return re.sub("[%s]" % "|".join(map(str,odd_values)), '', s)
