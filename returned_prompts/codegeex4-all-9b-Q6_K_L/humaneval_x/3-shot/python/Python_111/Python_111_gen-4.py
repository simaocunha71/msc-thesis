    count = {}
    for c in test:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    max_count = max(count.values(), default=0)
    result = {k: v for k, v in count.items() if v == max_count}

    return result

