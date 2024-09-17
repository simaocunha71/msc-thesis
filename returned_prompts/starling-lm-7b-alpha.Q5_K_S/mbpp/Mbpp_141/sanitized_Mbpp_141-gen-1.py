def pancake_sort(lst):
    """Sort a list of elements using pancake sort."""
    while lst:
        max_elem = max(lst)
        max_index = lst.index(max_elem)
        lst.remove(max_elem)
        lst.insert(0, max_elem)
        del lst[max_index + 1]
    return lst