def division_elements(tup1, tup2):
    return tuple(i / j for i, j in zip(tup1, tup2)) if len(tup1) == len(tup2) else None