    def strange_sort_helper(lst, min_max_switch=False):
        if len(lst) == 0:
            return []

        if min_max_switch:
            return strange_sort_helper(lst[:-1], min_max_switch=False) + [max(lst)] + strange_sort_helper(lst[:-1], min_max_switch=True)
        else:
            return strange_sort_helper(lst[:-1]) + [min(lst)]

    return strange_sort_helper(lst)


