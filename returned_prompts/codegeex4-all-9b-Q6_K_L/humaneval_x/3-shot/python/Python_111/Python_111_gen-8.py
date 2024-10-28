    counts = {}
    for c in test:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    max_count = max(counts.values())
    result = {k: v for k, v in counts.items() if v == max_count}

    return result

