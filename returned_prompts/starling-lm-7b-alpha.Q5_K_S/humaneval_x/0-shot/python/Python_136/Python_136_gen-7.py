
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    result = (None, None)
    for num in lst:
        if num < 0:
            if result[0] is None:
                result = (num, None)
            elif num > result[0]:
                result = (num, result[0])
        elif num > 0:
            if result[1] is None:
                result = (result[0], num)
            elif num < result[1]:
                result = (result[0], num)
    return result

# Test Cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
print(largest_smallest_integers([-1, -2, -3, -4, -5, -6]))  # (-6, None)
print(largest_smallest_integers([1, 2, 3, 4, 5, 6]))  # (None, 1)
print(largest_smallest_integers([-1, 1, 2, 3, 4, 5]))  # (-1, 1)








































