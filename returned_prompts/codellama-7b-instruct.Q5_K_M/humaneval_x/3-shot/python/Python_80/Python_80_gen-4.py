    if len(s) < 3:
        return False

    if s == s[::-1]:
        return True

    return False


