def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result