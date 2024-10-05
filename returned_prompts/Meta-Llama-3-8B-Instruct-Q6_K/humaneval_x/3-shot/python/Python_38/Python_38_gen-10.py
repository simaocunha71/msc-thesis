    result = ""
    group = ""
    for char in s:
        group += char
        if len(group) == 3:
            result += group[2] + group[0] + group[1]
            group = ""
    if group:
        result += group
    return result


