# Here is one possible solution to the problem:

def total_match(lst1, lst2):
    if len(lst1) < len(lst2):
        return lst1
    elif len(lst1) > len(lst2):
        return lst2
    else:
        return lst1

# Another possible solution:

def total_match(lst1, lst2):
    total1 = sum(len(word) for word in lst1)
    total2 = sum(len(word) for word in lst2)

    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1


# Or you can use built-in Python functions:

def total_match(lst1, lst2):
    if sum(map(len, lst1)) < sum(map(len, lst2)):
        return lst1
    elif sum(map(len, lst1)) > sum(map(len, lst2)):
        return lst2
    else:
        return lst1

# Or you can use list comprehension with built-in Python functions:

def total_match(lst1, lst2):
    total1 = sum([len(word) for word in lst1])
    total2 = sum([len(word) for word in lst2])

    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1

# Or you can use built-in Python functions with list comprehension:

def total_match(lst1, lst2):
    total1 = sum(len(word) for word in lst1)
    total2 = sum(len(word) for word in lst2)

    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1

# Or you can use built-in Python functions with generator expressions:

def total_match(lst1,