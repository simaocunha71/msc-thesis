    total = 0
    for idx, num in enumerate(lst):
        if idx % 3 == 0:
            total += num ** 2
        elif idx % 4 == 0:
            total += num ** 3
    return total

