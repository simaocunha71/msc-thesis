    freq_dict = {}
    max_freq = 0
    result = -1

    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        max_freq = max(max_freq, freq_dict[num])

    for num, freq in freq_dict.items():
        if freq >= num:
            result = max(result, num)

    return result

