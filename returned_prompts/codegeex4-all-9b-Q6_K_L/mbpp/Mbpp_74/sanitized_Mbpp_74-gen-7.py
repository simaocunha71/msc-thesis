def is_samepatterns(patterns, p):
    if len(patterns) != len(p):
        return False
    for i in range(len(patterns)):
        if patterns[i] != p[i]:
            return False
    return True