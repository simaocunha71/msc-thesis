    freq = {}
    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    max_num = -1
    for num, count in freq.items():
        if num > 0 and count >= num:
            max_num = num

    return max_num
