def merge_sorted_list(a, b, c):
    a.extend(b)
    a.extend(c)
    return sorted(a)