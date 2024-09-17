def recursive_list_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += recursive_list_sum(elem)
        else:
            total += elem
    return total