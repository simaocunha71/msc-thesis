

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    
    uniq = []
    for e in l:
        if(e not in uniq):
            uniq.append(e)
            
    return sorted(uniq, key=len)

print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))