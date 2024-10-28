def remove_odd(s):
    result = ""
    for i in s:
        if int(i) % 2 == 0:
            result += i
    return result