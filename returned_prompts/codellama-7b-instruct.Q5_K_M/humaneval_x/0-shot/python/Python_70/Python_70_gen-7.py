
def strange_sort_list(lst):
    return sorted(lst, key=lambda x: -x if x in lst[:1] else x)