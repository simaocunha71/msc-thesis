    if not test:
        return {}

    test = test.split()
    max_count = max(test.count(c) for c in set(test))
    return {c: test.count(c) for c in set(test) if test.count(c) == max_count}  # set(test) to remove duplicates


