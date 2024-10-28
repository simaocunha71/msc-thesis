    return [i if idx % 3 != 0 else sorted([x for x in l if idx % 3 == 0])[0] for idx, i in enumerate(l)]


