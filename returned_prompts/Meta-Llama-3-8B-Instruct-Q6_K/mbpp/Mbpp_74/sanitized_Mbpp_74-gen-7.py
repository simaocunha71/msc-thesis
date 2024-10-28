def is_samepatterns(patterns, sequences):
    if len(patterns) != len(sequences):
        return False
    for pattern, sequence in zip(patterns, sequences):
        if len(pattern) != len(sequence):
            return False
        for p, s in zip(pattern, sequence):
            if p != s:
                return False
    return True