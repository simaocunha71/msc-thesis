    freq = {}

    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    for key in freq.keys():
        if freq[key] >= key and key > 0:
            return key

    return -1


