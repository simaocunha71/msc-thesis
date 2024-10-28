def find_sum(lst):
    seen = set()
    total = 0
    for item in lst:
        if item not in seen:
            total += item
            seen.add(item)
    return total