    seen = set()
    return [x for x in numbers if x not in seen and not seen.add(x)]


