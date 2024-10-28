
def overlapping(seq1: list, seq2: list):
    return any(i in seq2 for i in seq1)


