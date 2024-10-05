    if len(s0) != len(s1):
        return False

    s0 = s0.replace(' ', '')
    s1 = s1.replace(' ', '')

    for c in s0:
        if c not in s1:
            return False

    return True


