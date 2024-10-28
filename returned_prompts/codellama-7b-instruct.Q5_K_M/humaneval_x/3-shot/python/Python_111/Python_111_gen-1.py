    hist = {}
    for c in test:
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1

    max_count = max(hist.values())
    result = {k: v for k, v in hist.items() if v == max_count}
    return result
