def search(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if l[0] != l[1]:
        return l[0]
    if l[-1] != l[-2]:
        return l[-1]
    mid = len(l) // 2
    if l[mid] != l[mid-1]:
        return l[mid]
    return search(l[:mid])