def unique_sublists(lists):
    result = {}
    for item in lists:
        if isinstance(item, list):
            item = tuple(sorted(item))
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result