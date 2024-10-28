"""
def frequency_lists(list_of_lists):
    result = {}
    for l in list_of_lists:
        for e in l:
            if e in result:
                result[e] += 1
            else:
                result[e] = 1
    return result
"""
