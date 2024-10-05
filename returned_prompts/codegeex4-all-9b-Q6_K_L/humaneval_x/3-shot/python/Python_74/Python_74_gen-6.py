    if sum(len(item) for item in lst1) == sum(len(item) for item in lst2):
        return lst1
    elif sum(len(item) for item in lst1) < sum(len(item) for item in lst2):
        return lst1
    else:
        return lst2

