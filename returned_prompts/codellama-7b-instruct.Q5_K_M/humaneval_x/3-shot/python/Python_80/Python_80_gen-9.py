    if len(s) < 3:
        return False

    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return False
    return True


