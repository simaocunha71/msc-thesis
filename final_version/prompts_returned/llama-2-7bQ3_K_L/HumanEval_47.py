

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        return None
    else:
        return _median(l)

def mean(l: list):
    '''Return mean of elements in the list l'''
    if not l:
        return 0
    elif len(l) == 1:
        return 1.0
    
    total = sum([item for item in l])
    return total / float(len(l))

def _median(l: list):
    '''Return median of elements in the list '''
    if not l:
        return None
    else:
        l.sort()
        
        num_items = len(l) - 1
        if num_items % 2 == 0:
            med = (l[num_items // 2] + l[num_items // 2 - 1]) / 2
        else:
            med = l[num_items//2]