    if len(lst) < 2:
        return None
    
    lst.sort()
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            return lst[i]
    
    return None

