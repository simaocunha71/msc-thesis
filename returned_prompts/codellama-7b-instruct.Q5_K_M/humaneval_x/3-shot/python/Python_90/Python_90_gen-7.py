    if len(lst) < 2:
        return None
    else:
        smallest = lst[0]
        smallest_idx = 0
        for i in range(1, len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
                smallest_idx = i
        if smallest_idx == 0:
            return lst[1]
        else:
            return lst[smallest_idx - 1]


