def unique_sublists(l):
    return {t:l.count(t) for t in map(tuple, l)}
