    l = sorted(l)
    mid = (len(l)-1) // 2
    return l[mid] if len(l) % 2 == 1 else (l[mid] + l[mid+1]) / 2


