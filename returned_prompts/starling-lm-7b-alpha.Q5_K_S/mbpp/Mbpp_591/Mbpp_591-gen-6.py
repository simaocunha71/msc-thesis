
def swap_List(lst):
    first = lst[0]
    last = lst[len(lst)-1]
    lst[0] = last
    lst[len(lst)-1] = first
    return lst


