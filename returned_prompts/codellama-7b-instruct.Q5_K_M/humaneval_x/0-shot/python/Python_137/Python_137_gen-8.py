
import re

def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, str):
        a = re.sub(",", ".", a)
        if float(a) > b:
            return a
        else:
            return b
    elif isinstance(b, str):
        b = re.sub(",", ".", b)
        if a > b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b