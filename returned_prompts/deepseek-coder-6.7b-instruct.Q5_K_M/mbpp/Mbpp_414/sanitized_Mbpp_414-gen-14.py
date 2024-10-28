def overlapping(seq1, seq2): 
    return any(value in seq1 for value in seq2)