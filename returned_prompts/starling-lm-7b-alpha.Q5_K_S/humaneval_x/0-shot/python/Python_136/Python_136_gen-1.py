
def largest_smallest_integers(lst):
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    negatives = [x for x in lst if x < 0]
    positives = [x for x in lst if x > 0]

    if len(negatives) == 0:
        a = None
    else:
        a = max(negatives)

    if len(positives) == 0:
        b = None
    else:
        b = min(positives)

    return (a, b)


# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
print(largest_smallest_integers([-1, -2, -3, 4, 5, 6]))  # (-3, 4)
print(largest_smallest_integers([-1, 0, 1, 2]))  # (None, 1)


# More test cases
print(largest_smallest_integers([-100, 100, 200, -50, 300, -200]))  # (-200, 100)
print(largest_smallest_integers([-1, -2, 1, 2, 3, 4]))  # (None,