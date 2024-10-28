
    negative_numbers = [i for i in lst if i < 0]
    positive_numbers = [i for i in lst if i > 0]

    if negative_numbers:
        largest_negative = max(negative_numbers)
    else:
        largest_negative = None

    if positive_numbers:
        smallest_positive = min(positive_numbers)
    else:
        smallest_positive = None

    return (largest_negative, smallest_positive)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)

# ----------------------------------------------
# Alternatively, you can use Python's built-in functions to find the 
# maximum and minimum of a list with conditions as follows:

def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) 
    '''

    largest_negative = max((i for i in lst if i < 0), default=None)
    smallest_positive = min((i for i in lst if i > 0), default=None)

    return (largest_negative, smallest_positive)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
<jupyter_output>
(None, 1)
(None, None)
