
def next_smallest(lst):
    if len(lst) < 2:
        return None
    return sorted(lst)[1]
