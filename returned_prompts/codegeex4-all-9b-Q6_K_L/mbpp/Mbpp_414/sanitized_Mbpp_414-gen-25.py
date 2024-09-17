def overlapping(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    return not set1.isdisjoint(set2)