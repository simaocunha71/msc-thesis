    evens = [n for (i, n) in enumerate(lst) if i % 2 == 0 and n % 2 == 0]
    return sum(evens)


