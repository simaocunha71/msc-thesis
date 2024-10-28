    def strange_sort(lst, index=0):
        if index == len(lst) - 1:
            return [lst[index]]
        return [lst[index]] + strange_sort(lst[index + 1:], index + 1)
    return strange_sort(lst)


