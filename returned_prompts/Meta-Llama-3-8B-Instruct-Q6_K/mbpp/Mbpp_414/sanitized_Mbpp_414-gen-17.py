def overlapping(seq1, seq2):
    for element in seq1:
        if element in seq2:
            return True
    return False