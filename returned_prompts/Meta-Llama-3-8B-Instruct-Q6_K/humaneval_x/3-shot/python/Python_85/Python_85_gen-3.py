    return sum([x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0])  # use list comprehension to create a new list with even elements at odd indices, then sum them up


