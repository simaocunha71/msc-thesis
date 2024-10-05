    return sorted([l[x] for x in range(len(l)) if x % 3 == 0]) + [l[x] for x in range(len(l)) if x % 3 != 0]


