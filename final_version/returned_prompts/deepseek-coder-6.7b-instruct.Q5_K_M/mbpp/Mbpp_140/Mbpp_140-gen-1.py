def extract_singly(lst):
    result = []
    for sublist in lst:
        if isinstance(sublist, tuple):
            result.extend(sublist)
        else:
            result.append(sublist)
    return set(result)

assert set(extract_singly([(3, 4, 5),  (4, 5, 7),  (1, 4)])) == set([3, 4, 5, 7, 1])


