"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""

def remove_all_spaces(str):
    return str.translate(dict((ord(c), None) for c in ' \t\n'))