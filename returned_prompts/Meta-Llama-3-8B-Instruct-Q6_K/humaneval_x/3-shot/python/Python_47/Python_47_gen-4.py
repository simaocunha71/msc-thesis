    l.sort()
    n = len(l)
    if n % 2 == 0:
        mid1 = l[n//2 - 1]
        mid2 = l[n//2]
        return (mid1 + mid2) / 2
    else:
        return l[n//2]  # The middle element


