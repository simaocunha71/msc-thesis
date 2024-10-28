def remove_duplicates(numbers):
    seen = set()
    seen_add = seen.add
    return [x for x in numbers if not (x in seen or seen_add(x))]
