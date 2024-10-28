    from collections import Counter

    counter = Counter(lst)
    result = -1

    for num, freq in counter.items():
        if freq >= num and num > result:
            result = num

    return result

