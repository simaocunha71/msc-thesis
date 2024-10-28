    if len(lst) < 2:
        return None
    else:
        min_val = min(lst)
        lst.remove(min_val)
        min_val = min(lst)
        return min_val


