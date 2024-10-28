def histogram(test):
    if len(test) == 0:
        return {}
    test = test.split(' ')
    counts = {}
    for letter in test:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values())
    return {k: v for k, v in counts.items() if v == max_count}