def flatten_list(lst):
    return [item for sublist in lst for item in sublist] if lst else []
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    stack = [lst]
    while stack:
        item = stack.pop()
        if type(item) == list:
            stack.extend(item)
        else:
            result.append(item)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
    # or
    result = []