def max_length(lists):
    if not lists: return None
    max_len, max_sublist = len(lists[0]), lists[0]
    for sublist in lists[1:]:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_sublist = sublist
    return max_len, max_sublist
