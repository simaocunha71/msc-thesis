def overlapping(seq1, seq2):
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                return True
    return False