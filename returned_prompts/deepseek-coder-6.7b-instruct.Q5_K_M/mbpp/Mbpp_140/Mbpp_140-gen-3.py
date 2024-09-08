"""
def extract_singly(lst):
    result = []
    for i in lst:
        if isinstance(i, tuple):
            result.extend(i)
        else:
            result.append(i)
    return result

print(set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])))
"""

