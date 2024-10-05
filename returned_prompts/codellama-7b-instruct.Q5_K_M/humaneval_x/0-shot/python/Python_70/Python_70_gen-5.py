
def strange_sort_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        lst.sort()
        min = lst[0]
        max = lst[-1]
        if min == max:
            return lst
        else:
            lst.remove(min)
            lst.remove(max)
            return [min] + [max] + strange_sort_list(lst)
