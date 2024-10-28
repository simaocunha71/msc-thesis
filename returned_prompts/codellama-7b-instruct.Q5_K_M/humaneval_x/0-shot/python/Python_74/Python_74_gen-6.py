
def total_match(lst1, lst2):
    return sorted(lst2, key=lambda x: len(x)) if sum(map(len, lst1)) < sum(map(len, lst2)) else sorted(lst1, key=lambda x: len(x))