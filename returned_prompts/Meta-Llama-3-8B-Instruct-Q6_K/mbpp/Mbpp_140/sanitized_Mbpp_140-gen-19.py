def extract_singly(lst):
    result = []
    for sublist in lst:
        result.extend(sublist)
    return set(result)