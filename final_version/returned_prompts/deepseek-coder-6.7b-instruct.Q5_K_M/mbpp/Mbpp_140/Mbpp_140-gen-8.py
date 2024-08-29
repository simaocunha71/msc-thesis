"""
def extract_singly(lst):
    result = []
    for i in lst:
        if isinstance(i, tuple):
            result.extend(i)
        else:
            result.append(i)
    return set(result)
"""

