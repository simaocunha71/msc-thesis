    return sorted([s for s in lst if len(s) % 2 == 0], key=lambda x: (len(x), x))  # or use sorted(lst, key=lambda x: (len(x), x)) if you want to sort the whole list


