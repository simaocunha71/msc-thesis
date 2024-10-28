    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda x: (len(x), x))  # filter odd length strings and sort based on length and then alphabetically


