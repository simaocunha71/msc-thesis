def two_unique_nums(*lists):
    result = []
    for lst in lists:
        for num in lst:
            if num not in result:
                result.append(num)
    return result