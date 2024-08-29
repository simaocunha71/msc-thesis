
def overlapping(seq1, seq2):
    return any(item in seq1 for item in seq2)

print(overlapping([1,2,3,4,5],[6,7,8,9]))

