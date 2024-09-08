
def overlapping(seq1, seq2):
    for item in seq1:
        if item in seq2:
            return True
    return False

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False

# OR

def overlapping(seq1, seq2):
    return any(item in seq2 for item in seq1)

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False

# OR

def overlapping(seq1, seq2):
    return bool(set(seq1) & set(seq2))

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False

# OR

def overlapping(seq1, seq2):
    return set(seq1).intersection(seq2) != set()

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False

# OR

def overlapping(seq1, seq2):
    return any(i in seq1 for i in seq2)

print(overlapping([1,2,3,4,5],[6,7,8,9])) # False
"""


assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[3,4,5,6,7]) == True
assert overlapping([1,2,3,4,5],[6,7,8]) == False
assert overlapping(['a','b','c'],['d','e','f','a']) == True
assert overlapping(['a','b','c'],['d','e','f']) == False
"""
"""



