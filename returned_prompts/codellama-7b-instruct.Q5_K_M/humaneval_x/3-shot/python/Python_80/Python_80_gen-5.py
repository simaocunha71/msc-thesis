    if len(s) < 3:
        return False
    for idx in range(len(s) - 2):
        if s[idx] == s[idx + 1] == s[idx + 2]:
            return False
    return True
