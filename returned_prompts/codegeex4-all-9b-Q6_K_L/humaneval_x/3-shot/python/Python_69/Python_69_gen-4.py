    freq = {}

    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if num <= count:
            return num

    return -1

