def pair_wise(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    result = []
    for item, count in freq.items():
        for i in range(count):
            if i == 0:
                result.append((item, item))
            if i < count - 1:
                result.append((item, item))
    return result