def is_samepatterns(patterns, seq):
    if len(patterns) != len(seq):
        return False
    for i in range(len(patterns)):
        if patterns[i] != seq[i]:
            return False
    return True