    if len(lst) == 0: return 0
    else:
        return sum([x**2 for x in lst if (x > 0) and (x % 2 != 0)])


