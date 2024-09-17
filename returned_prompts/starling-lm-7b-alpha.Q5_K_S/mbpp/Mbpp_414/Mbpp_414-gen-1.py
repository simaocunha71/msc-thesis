
def overlapping(seq1, seq2):
    for elem in seq1:
        if elem in seq2:
            return True
    return False


