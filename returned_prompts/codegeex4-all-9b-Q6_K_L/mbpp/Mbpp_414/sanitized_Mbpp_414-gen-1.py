def overlapping(seq1, seq2):
    for item in seq1:
        if item in seq2:
            return True
    return False