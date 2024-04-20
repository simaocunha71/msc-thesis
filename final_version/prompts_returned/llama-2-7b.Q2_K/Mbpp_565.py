"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
import re
def split(s):
    return [e for s in re.split("(?<=[ab])",s)] if s[0] != '' else []
