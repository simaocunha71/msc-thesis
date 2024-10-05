    lst = [word for word in lst if len(word) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))  # Sort by length, then alphabetically


