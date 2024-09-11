def remove_all_spaces(s):
    result = ""
    for i in range(len(s)):
        if s[i].isspace():
            continue
        result += s[i]
    return result