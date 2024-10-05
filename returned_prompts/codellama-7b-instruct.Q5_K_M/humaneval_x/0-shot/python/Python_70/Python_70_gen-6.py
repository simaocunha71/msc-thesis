
def strange_sort_list(lst):
    if len(lst) <= 1:
        return lst

    min_val = min(lst)
    max_val = max(lst)

    if min_val == max_val:
        return [min_val]

    return [min_val, max_val] + strange_sort_list([x for x in lst if x != min_val and x != max_val])
