def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    
    result = [[lst[0]]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            result[-1].append(lst[i])
        else:
            result.append([lst[i]])
    return result