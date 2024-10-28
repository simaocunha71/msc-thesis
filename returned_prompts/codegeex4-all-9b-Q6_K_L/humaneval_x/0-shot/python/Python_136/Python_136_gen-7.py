def largest_smallest_integers(lst):
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]

    if negatives:
        a = max(negatives)
    else:
        a = None

    if positives:
        b = min(positives)
    else:
        b = None

    return (a, b)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # (None, 1)
print(largest_smallest_integers([])) # (None, None)
print(largest_smallest_integers([0])) # (None, None)