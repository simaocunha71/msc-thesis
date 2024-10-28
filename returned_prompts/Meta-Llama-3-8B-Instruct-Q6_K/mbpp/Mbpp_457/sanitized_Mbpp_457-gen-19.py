def Find_Min(lst):
    if not lst or not any(lst):
        return []
    min_len = min(len(sublist) for sublist in lst)
    return next(sublist for sublist in lst if len(sublist) == min_len)