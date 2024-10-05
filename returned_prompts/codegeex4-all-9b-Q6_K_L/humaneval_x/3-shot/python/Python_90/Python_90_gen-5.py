    if len(lst) < 2 or len(set(lst)) < 2:
        return None

    smallest = min(lst)
    lst.remove(smallest)
    return min(lst)