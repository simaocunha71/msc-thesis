
def strange_sort_list(lst):
    return sorted(lst, key=lambda x: (x, -x))

or

def strange_sort_list(lst):
    lst.sort(key=lambda x: (x, -x))
    return lst


