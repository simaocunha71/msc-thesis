def overlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False