def unique_Element(lst):
    element_set = set(lst)
    if len(element_set) == 1:
        return next(iter(element_set))
    else:
        return None