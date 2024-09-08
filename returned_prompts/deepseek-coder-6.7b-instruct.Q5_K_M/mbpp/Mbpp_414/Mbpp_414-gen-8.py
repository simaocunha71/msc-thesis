
def overlapping(seq1, seq2):
    for i in seq1:
        if i in seq2:
            return True
    return False

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False

