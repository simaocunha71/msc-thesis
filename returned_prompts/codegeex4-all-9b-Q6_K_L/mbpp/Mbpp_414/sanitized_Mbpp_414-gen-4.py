def overlapping(seq1, seq2):
    for value in seq1:
        if value in seq2:
            return True
    return False