

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l: return None
    # sort list from smallest to largest element
    sorted_list = sorted(l, reverse=True)
    assert len(sorted_list) >= 2 and sorted_list[0] < sorted_list[-1], "must have at least two elements"
    
    if (len(sorted_list)) == 2: return sorted_list[1] # single element case -- return the only element in the list
    elif len(sorted_list) == 3 and sorted_list[0] < sorted_list[-1]:
        # two elements, check whether we have an odd number of elements
        if (len(l)) % 2 == 1: median = (sorted_list[0] + sorted_list[int((len(l)/2) - 1)] ) / 2.0
    else: median = (sorted_list[int((len(sorted_list)/2))) + sorted_list[-1])/2.0
    
    return median
