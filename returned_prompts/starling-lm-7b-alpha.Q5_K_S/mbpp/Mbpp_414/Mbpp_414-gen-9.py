def overlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False




"""
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""


def overlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False


# Driver code

"""
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""








"""
def checkOverlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False


# Driver Code
checkOverlapping([1, 2, 3, 4, 5], [6, 7, 8, 9])

"""



























"""
def checkOverlapping(seq1, seq2):
    if len(seq1) == 0 or len(seq2) == 0:
        return False
    for i in range(len(seq1)):
        if seq1[i] in seq2:
            return True
    return False


# Driver Code
checkOverlapping([1, 2, 3, 4, 5], [6, 7, 8, 9])

"""




























"""
def checkOverlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False


# Driver Code
checkOverlapping([1, 2, 3, 4, 5], [6, 7, 8, 9])

"""





















"""
def checkOverlapping(seq1, seq