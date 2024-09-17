def is_samepatterns(patterns, sequence):
    if len(patterns) != len(sequence):
        return False
    for pattern, seq in zip(patterns, sequence):
        if pattern != seq:
            return False
    return True