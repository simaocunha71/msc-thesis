def first_odd(lst):
    for i in range(0,len(lst)):
        if lst[i]%2!=0:
            return lst[i]
    return -1