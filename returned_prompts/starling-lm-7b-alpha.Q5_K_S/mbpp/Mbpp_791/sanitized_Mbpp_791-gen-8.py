import sys
def remove_nested(t):
    result = []
    for i in t:
        if not isinstance(i, tuple):
            result.append(i)
        else:
            result.append(remove_nested(i))
    return tuple(result)