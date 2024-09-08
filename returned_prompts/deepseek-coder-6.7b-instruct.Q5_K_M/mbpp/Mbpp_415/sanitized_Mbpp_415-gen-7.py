def max_Product(lst):
    lst.sort() # sort the list in ascending order
    if lst[0] < 0 and lst[1] < 0: # if first two numbers are negative
        return (lst[0], lst[1]) if lst[0] * lst[1] > lst[-1] * lst[-2] else (lst[-1], lst[-2])
    else:
        return (lst[-1], lst[-2])