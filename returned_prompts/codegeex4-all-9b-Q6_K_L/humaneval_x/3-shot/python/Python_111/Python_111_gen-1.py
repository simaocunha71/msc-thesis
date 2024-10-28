    from collections import Counter

    if not test:
        return {}

    letters = test.split()
    counter = Counter(letters)
    max_count = max(counter.values())
    result = {k: v for k, v in counter.items() if v == max_count}

    return result

