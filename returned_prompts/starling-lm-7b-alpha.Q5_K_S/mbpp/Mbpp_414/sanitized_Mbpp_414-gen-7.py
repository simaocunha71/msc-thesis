def overlapping(seq1, seq2):
    return any(value in seq2 for value in seq1)