
def overlapping(seq1:list,seq2:list)->bool:
    for i in seq1:
        if i in seq2:
            return True
    return False


