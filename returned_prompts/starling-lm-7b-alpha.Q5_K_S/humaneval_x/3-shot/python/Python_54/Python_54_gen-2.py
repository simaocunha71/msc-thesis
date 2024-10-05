    s0 = sorted(s0)
    s1 = sorted(s1)
    if len(s0) != len(s1):
        return False
    for i in range(len(s0)):
        if s0[i] != s1[i]:
            return False
    return True


