
def overlapping(seq1, seq2):
    return any(i in seq1 for i in seq2)

print(overlapping([1,2,3,4,5],[6,7,8,9]))

# Explanation:
# The function overlapping takes two sequences seq1 and seq2 as input. It returns True if any value in seq2 exists in seq1. 
# This is done using the any() function combined with a generator expression. 
# The any() function returns True if any of the elements in the iterable are true. 
# The generator expression checks if each element in seq2 is in seq1. If any of them are, it returns True.
# Otherwise, it returns False.


