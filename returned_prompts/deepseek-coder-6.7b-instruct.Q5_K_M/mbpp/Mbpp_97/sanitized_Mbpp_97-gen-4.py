def frequency_lists(lst):
    result = {}
    for sublist in lst:
        for item in sublist:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result