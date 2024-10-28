def overlapping(seq1, seq2):
    return any(i in seq2 for i in seq1) or any(i in seq1 for i in seq2)  # O(n*m) time complexity