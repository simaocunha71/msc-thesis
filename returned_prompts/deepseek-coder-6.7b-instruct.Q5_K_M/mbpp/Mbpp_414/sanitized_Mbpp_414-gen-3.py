def overlapping(seq1, seq2):
    for i in seq1:
        if i in seq2:
            return True
    return False