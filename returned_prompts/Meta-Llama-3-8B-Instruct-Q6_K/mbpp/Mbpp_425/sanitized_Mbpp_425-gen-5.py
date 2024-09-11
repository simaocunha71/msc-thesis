def count_element_in_list(lists, target):
    return sum(1 for lst in lists if target in lst)  # or sum(lst.count(target) for lst in lists)