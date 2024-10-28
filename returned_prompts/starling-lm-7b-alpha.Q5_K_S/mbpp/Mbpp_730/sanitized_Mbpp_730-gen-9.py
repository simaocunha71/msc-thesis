def consecutive_duplicates(lst):
    """
    Remove consecutive duplicates from a given list.
    """
    if not lst:
        return []
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result