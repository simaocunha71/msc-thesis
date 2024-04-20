"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""

def median(l1, l2):
    return (len(l1 + l2)) / 2 if len(l1 + l2) % 2 else (int((len(l1 + l2) + 1)/2) / 2)
