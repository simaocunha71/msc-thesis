from random import randrange
def pancake_sort(lst):
    for i in range(len(lst)):
        max_idx = randrange(len(lst))
        max_val = lst[max_idx]
        min_idx = lst.index(max_val)
        if max_idx != min_idx:
            lst[max_idx], lst[min_idx] = lst[min_idx], lst[max_idx]
    return lst