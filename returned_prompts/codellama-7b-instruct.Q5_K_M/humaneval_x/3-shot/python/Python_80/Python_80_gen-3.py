    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i:i+3] in s[i+1:]:
            return False

    return True


