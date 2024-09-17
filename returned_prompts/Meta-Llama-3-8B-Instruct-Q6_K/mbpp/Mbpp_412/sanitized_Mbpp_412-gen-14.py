def remove_odd(lst):
    for i in lst[:]:
        if i % 2 != 0:
            lst.remove(i)
    return lst