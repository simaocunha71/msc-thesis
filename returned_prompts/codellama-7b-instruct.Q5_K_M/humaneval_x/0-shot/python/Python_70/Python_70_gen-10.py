
def strange_sort_list(lst):
    if not lst:
        return lst
    return sorted(lst, key=lambda x: (x, -x))
