    from collections import Counter

    counter = Counter(lst)
    result = -1
    for num, freq in counter.items():
        if num > 0 and freq >= num:
            result = num
            break

    return result


