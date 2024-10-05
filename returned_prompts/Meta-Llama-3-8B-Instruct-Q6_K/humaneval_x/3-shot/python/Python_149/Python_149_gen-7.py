    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda s: (len(s), s))  # [1]


