
    from collections import defaultdict
    d = defaultdict(int)
    for c in test:
        d[c] += 1
    max_count = max(d.values())
    return {k: v for k, v in d.items() if v == max_count}


