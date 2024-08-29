def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(swap_List([12, 35, 9, 56, 24]))


