def is_samepatterns(patterns, sequence):
    if len(patterns) != len(sequence):
        return False
    for i in range(len(patterns)):
        if patterns[i] != str(len(set([x for x in sequence[:i+1] if sequence.count(x) > 1]))):
            return False
    return True