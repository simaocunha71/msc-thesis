def interleave_lists(lists):
    if not lists:
        return []
    result = []
    for i in range(len(lists[0])):
        for lst in lists:
            result.append(lst[i])
    return result
