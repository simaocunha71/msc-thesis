def is_samepatterns(patterns, pattern):
    if len(patterns) != len(pattern):
        return False
    for i in range(len(patterns)):
        if patterns[i] != pattern[i]:
            return False
    return True