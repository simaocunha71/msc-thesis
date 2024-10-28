def overlapping(seq1, seq2):
    for x in seq1:
        for y in seq2:
            if x == y:
                return True
    return False