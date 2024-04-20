"""
Write a function to convert a string to a list of strings split on the space character.
assert string_to_list("python programming")==['python','programming']
"""

def string_to_list(string):
    return [s[1:].rstrip() for s in string.split(' ')]
\end{code}