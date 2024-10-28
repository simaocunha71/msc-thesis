def frequency_lists(lst):
    result = {}
    for i in lst:
        for j in i:
            if j in result:
                result[j] += 1
            else:
                result[j] = 1
    return result