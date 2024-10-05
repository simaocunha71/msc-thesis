    result = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            result += group[2] + group[0] + group[1]
        else:
            result += group
    return result


