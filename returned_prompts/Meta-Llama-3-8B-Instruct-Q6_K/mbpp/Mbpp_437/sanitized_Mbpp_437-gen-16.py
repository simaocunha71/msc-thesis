def remove_odd(s):
    result = ""
    for i, c in enumerate(s):
        if i % 2 == 0:
            result += c
    return result