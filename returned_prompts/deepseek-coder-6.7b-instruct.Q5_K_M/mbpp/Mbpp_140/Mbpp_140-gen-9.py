
def extract_singly(lst):
    result = []
    for i in lst:
        if isinstance(i, tuple):
            result.extend(i)
        else:
            result.append(i)
    return set(result)

assert set(extract_singly([(3, 4, 5),  (4, 5, 7),  (1, 4)])) == set([3, 4, 5, 7, 1])

"""
