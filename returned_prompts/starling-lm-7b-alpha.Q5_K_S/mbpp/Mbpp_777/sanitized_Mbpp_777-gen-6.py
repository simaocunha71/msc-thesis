def find_sum(lst):
    seen = set()
    total = 0
    for i in lst:
        if i not in seen:
            total += i
            seen.add(i)
    return total