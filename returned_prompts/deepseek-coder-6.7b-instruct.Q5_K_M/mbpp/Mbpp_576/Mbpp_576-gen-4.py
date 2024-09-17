
def is_Sub_Array(A, B):
    lenA = len(A)
    lenB = len(B)
    i = 0
    j = 0
    while i < lenA and j < lenB:
        if A[i] == B[j]:
            j += 1
        i += 1
    return j == lenB


