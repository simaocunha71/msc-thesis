    from collections import defaultdict
    result = defaultdict(int)
    for letter in test:
        result[letter] += 1
    return dict(result)


