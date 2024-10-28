def overlapping(seq1, seq2):
    for i in seq1:
        for j in seq2:
            if i == j:
                return True
    return False