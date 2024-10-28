    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_freq = 0
    max_num = -1
    for num, freq in counts.items():
        if freq >= num and freq > max_freq:
            max_freq = freq
            max_num = num

    return max_num

