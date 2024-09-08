def overlapping(seq1, seq2):
    for x in seq1:
        if x in seq2:
            return True
    return False