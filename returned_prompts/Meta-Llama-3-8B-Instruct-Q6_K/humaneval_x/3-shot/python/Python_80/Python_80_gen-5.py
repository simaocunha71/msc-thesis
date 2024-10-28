    if len(s) < 3:
        return False
    for i in range(0, len(s) - 2):
        if len(set(s[i:i+3])) < 3:
            return False
    return True


