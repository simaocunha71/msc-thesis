    lst = [s for s in lst if len(s) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))  # Sort by length then alphabetically


