    from collections import Counter
    counter = Counter(test)
    return counter.most_common(1)[0] if counter else {}


