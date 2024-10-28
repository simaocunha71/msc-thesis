def remove_odd(s):
    odd = 0
    while odd < len(s):
        if ord(s[odd]) % 2 != 0:
            s = s[:odd] + s[odd + 1:]
        else:
            odd += 1
    return s