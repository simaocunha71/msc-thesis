    from collections import Counter

    counter = Counter(test.split())
    max_count = max(counter.values())

    return {key: value for key, value in counter.items() if value == max_count}

