def sum_in_range(l,r):
    if l%2 == 0 and r%2 == 0:
        return l + r
    elif l%2 != 0 and r%2 != 0:
        return (l + r) + sum_in_range(l+1,r-1)
    else:
        if l%2 != 0:
            return (l + r) + (l + 1)//2
        else:
            return (l + r) + r//2