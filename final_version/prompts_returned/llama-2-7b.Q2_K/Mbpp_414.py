"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""

def is_overlap(a, b):
    """Test if arrays have any element in common."""
    s = set(a).intersection(b)
    return s

if __name__=="__main__":
    assert is_overlap([1,2],[3]) == True