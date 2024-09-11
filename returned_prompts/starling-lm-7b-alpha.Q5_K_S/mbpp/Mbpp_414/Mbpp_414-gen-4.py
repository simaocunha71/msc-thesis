def overlapping(seq1,seq2):
    """
    Returns True if any value in the first sequence exists in the second sequence, and False otherwise.

    Parameters:
    seq1 (list): a list of integers
    seq2 (list): a list of integers

    Returns:
    bool: True if any value in seq1 exists in seq2, and False otherwise
    """
    for i in seq1:
        if i in seq2:
            return True
    return False

# Test the function
print(overlapping([1,2,3,4,5],[6,7,8,9]))  # should print False
print(overlapping([1,2,3,4,5],[3,4,5,6]))  # should print True





"""
Correct Solution:
"""
def overlapping(seq1,seq2):
    """
    Returns True if any value in the first sequence exists in the second sequence, and False otherwise.

    Parameters:
    seq1 (list): a list of integers
    seq2 (list): a list of integers

    Returns:
    bool: True if any value in seq1 exists in seq2, and False otherwise
    """
    for i in seq1:
        if i in seq2:
            return True
    return False

# Test the function
print(overlapping([1,2,3,4,5],[6,7,8,9]))  # should print False
print(overlapping([1,2,3,4,5],[3,4,5,6]))  # should print True





"""
Correct Solution:
"""
def overlapping(seq1,seq2):
    """
    Returns True if any value in the first sequence exists in the second sequence, and False otherwise.

    Parameters:
    seq1 (list): a list of integers
    seq2 (list): a list of integers

    Returns:
    bool: True if any value in seq1 exists in seq2, and False otherwise
    """
    for i in seq1:
        if i in seq2:
            return True
    return False

# Test