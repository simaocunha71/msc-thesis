"""
def extract_even(t):
    result = []
    for i in t:
        if isinstance(i, tuple):
            result.append(extract_even(i))
        else:
            if i % 2 == 0:
                result.append(i)
    return tuple(result)
"""
