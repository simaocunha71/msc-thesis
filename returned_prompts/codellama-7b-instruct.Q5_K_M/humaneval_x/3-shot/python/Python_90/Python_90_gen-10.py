    if len(lst) < 2:
        return None
    else:
        smallest = min(lst)
        for i in range(len(lst)):
            if lst[i] != smallest:
                return lst[i]


