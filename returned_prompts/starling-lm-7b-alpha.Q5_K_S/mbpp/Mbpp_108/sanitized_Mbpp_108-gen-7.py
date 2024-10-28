def merge_sorted_list(l1, l2, l3):
    '''
    Merge three lists into a single sorted list
    '''
    res = l1 + l2 + l3
    res.sort()
    return res