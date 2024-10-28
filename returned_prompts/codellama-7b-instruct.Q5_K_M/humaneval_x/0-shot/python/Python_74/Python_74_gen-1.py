
def total_match(lst1, lst2):
    if not lst1 and not lst2:
        return []
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    length1 = sum(len(x) for x in lst1)
    length2 = sum(len(x) for x in lst2)
    if length1 > length2:
        return lst2
    return lst1
