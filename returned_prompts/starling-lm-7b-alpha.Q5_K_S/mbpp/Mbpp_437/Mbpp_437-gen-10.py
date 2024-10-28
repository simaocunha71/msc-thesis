
def remove_odd(s):
    result = ""
    for c in s:
        if int(c) % 2 == 0:
            result += c
    return result


