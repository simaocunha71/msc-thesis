    if len(strings) == 0:
        return None
    result = ""
    for string in strings:
        if len(string) > len(result):
            result = string
    return result


