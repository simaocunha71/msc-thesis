    l = sorted(l)
    return l[len(l)//2] if len(l) % 2 else (l[len(l)//2] + l[(len(l)//2)-1]) / 2.0


