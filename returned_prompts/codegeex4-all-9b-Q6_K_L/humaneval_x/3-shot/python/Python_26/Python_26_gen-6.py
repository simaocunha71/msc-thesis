    seen = set()

    return [num for num in numbers if num not in seen and seen.add(num)]


