

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    
    unique_l1 = set(l1)
    for num in l2:
        if num not in unique_l1:
            return []
    
    return common_recursive([l1,l2], [], len(unique_l1))
    
def common_recursive(l1: list, l2: list, counter: int) ->list:
    if (len(l1) == 0):
        return []
    
    l3 = common(l1[:counter], l2[:counter]) # only compare first half of the lists
    counter += 1
    l4 = common_recursive(l1[counter:], l2[counter:], counter)
    if len(l3) != 0 and len(l4) != 0:
        return [item for sublist in (l3, l4)]
    
    else:
        counter +=1
        
    return []
