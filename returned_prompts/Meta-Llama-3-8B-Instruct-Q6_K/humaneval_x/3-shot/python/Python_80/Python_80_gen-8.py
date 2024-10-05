    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False

    return True
# or
def is_happy(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if set(s[i:i+3]) != set([s[i], s[i+1], s[i+2]]):
            return False

    return True


