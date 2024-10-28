def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    return (max(negatives) if negatives else None, min(positives) if positives else None)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)