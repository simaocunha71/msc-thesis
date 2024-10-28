def consecutive_duplicates(lst):
    result = []
    for num in lst:
        if not result or num != result[-1]:
            result.append(num)
    return result