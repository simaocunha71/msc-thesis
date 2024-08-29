
def overlapping(seq1, seq2):
    return any(item in seq1 for item in seq2)

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False
print(overlapping([1,2,3,4,5],[1,2,3,4,5])) # True
print(overlapping([1,2,3,4,5],[4,5,6,7])) # True
"""
This function uses the built-in function any() and a generator expression to check whether any element in seq2 exists in seq1.
"""

"""
