def overlapping(seq1, seq2):
    return any(value in seq2 for value in seq1)


"""
def overlapping(seq1, seq2):
    for value in seq1:
        if value in seq2:
            return True
    return False
"""

# Test
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[2,3,4,5,6]) == True

# Test with one-element sequences
assert overlapping([1],[1,2,3]) == True
assert overlapping([1],[2,3]) == False

# Test with empty sequences
assert overlapping([],[]) == False
assert overlapping([1],[]) == False

# Test with one-element sequence and empty sequence
assert overlapping([],[1]) == False

# Test with empty sequence and one-element sequence
assert overlapping([1],[]) == False

# Test with empty sequence and empty sequence
assert overlapping([],[]) == False

# Test with empty sequence and one-element sequence
assert overlapping([],[1]) == False

# Test with one-element sequence and empty sequence
assert overlapping([1],[]) == False

# Test with one-element sequence and one-element sequence
assert overlapping([1],[1]) == True

# Test with one-element sequence and one-element sequence
assert overlapping([1],[2]) == False

# Test with one-element sequence and one-element sequence
assert overlapping([2],[1]) == False

# Test with one-element sequence and one-element sequence
assert overlapping([1],[1]) == True

# Test with one-element sequence and one-element sequence
assert overlapping([1],[2]) == False

# Test with one-element sequence and one-element sequence
assert overlapping([2],[1]) == False

# Test with one-element sequence and one-element sequence
assert overlapping([1],[1]) == True

# Test with one-element sequence and one-element sequence
assert overlapping([1],[2]) == False

# Test with one