    def largest_smallest_integers(lst):
        a = max(i for i in lst if i < 0)
        b = min(i for i in lst if i > 0)
        return (a, b) if a is not None and b is not None else (None, None)

    return largest_smallest_integers(lst)




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

    a = max(i for i in lst if i < 0)
    b = min(i for i in lst if i > 0)
    return (a, b) if a is not None and b is not None else (None, None)

    return largest_smallest_integers(lst)





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

    a = max(i for i in lst if i < 0)
    b = min(i for i in lst if i >