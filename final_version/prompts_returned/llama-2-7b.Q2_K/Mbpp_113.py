"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
import re

def is_int(s):
    p = ''
    for c in s:
        if c != '0' and c<='9':
            p +=c
        else:
            break
    try:
        return int(p)
    except ValueError:
        return False

    """Test your code by entering "python" as input"""
if __name__ == '__main__':
    print check_integer('123456')
