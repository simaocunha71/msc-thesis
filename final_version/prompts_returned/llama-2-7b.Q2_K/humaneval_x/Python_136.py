
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

    def find_largest(lst):
        if len(lst) >= 2:
            if lst[1] < lst[0]: # check to see if the largest integer is negative or positive.
                return lst[1], lst[0]
            else:
                return lst[0], lst[1]
    def find_smallest(lst):
        if len(lst) >= 2:
            return lst[1], lst[0]
    return (find_largest(lst), find_smallest(lst))
