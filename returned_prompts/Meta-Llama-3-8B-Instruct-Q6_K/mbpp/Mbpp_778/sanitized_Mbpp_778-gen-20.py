def pack_consecutive_duplicates(lst):
    result = []
    if not lst:
        return result
    
    current_group = [lst[0]]
    
    for num in lst[1:]:
        if num == current_group[-1][0]:
            current_group.append(num)
        else:
            result.append(current_group)
            current_group = [num]
    
    result.append(current_group)
    return result